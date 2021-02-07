#!/usr/local/bin/python3
import sys


def find_max_concurrent_video_calls(*input_files):
    """
    Finds the maximum number of video calls we see at once in the logs.
    
    The format of the input file is
    1594857958 twilio call-ended room_e7c6d80181b6dc350c4258747ceb6211    sessionId RMb82221a073f0e618d10bad6c5ce5c5c5
    1594857997 twilio call-started room_6399485e947a33f0d39e45dd8ac27784    sessionId RM3d4145988f25eabb5fcc5c545bf42115
    1594858000 twilio call-started room_1042426e80ce705744ee40be1151a6d0    sessionId RM8326f408e5fb27567fbd8b00805821fc
    1594858002 twilio call-missed room_1042426e80ce705744ee40be1151a6d0    sessionId RM8326f408e5fb27567fbd8b00805821fc
    and it is assumed that the lines are sorted by epoch time which is the first number.
    """
    max_count = 0  # Maximum number of simultaneous video calls seen
    current_count = 0  # Number of simultaneous video calls for current line
    previous_timestamp = 0  # For checking if we receive records out of order
    cur_calls = {}  # Calls currently in progress. Value is start timestamp.
    ended_calls = {} # Calls already ended. Key is the call end time. Used to detect sessions which are already ended.
    for f in input_files:
        for line in open(f[0]):
            line = line.rstrip()  # Remove newline
            rec = line.split()
            if len(rec) != 6:
                print("Bad line format: " + line, file=sys.stderr)
                next
            timestamp, x, op, room, x, session_id = rec
            timestamp = int(timestamp)
            if timestamp < previous_timestamp:
                print('Records out of order. "%s" timestamp less than %u' % (line, previous_timestamp), file=sys.stderr)
                sys.exit(1)
            if op == "call-started":
                cur_calls[session_id] = timestamp
                current_count += 1
                if current_count > max_count:
                    max_count = current_count
            elif op == "call-missed" or op == "call-ended" or op == "call-rejected":
                if session_id in cur_calls.keys():
                    current_count -= 1
                    del cur_calls[session_id]
                    ended_calls[session_id] = timestamp
                elif session_id not in ended_calls.keys(): # ignore if call was already marked as ended.
                    print('Have an ending record for session id "%s" but no start record' % session_id, file=sys.stderr)
            else:
                print("Unknown op " + op, file=sys.stderr)
                sys.exit(1)
            previous_timestamp = timestamp
    if len(cur_calls) > 0:
        print(F"Saw start records for these calls but no end records:{len(cur_calls)}",
              file=sys.stderr)  # 220 such calls
        for k in cur_calls: print(k)
    max_count -= len(cur_calls)  # Calls started but not finished
    return max_count


if __name__ == "__main__":
    print("Maximum number of concurrent video calls is %u" % find_max_concurrent_video_calls(sys.argv[1:]))
