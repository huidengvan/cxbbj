# shift from ... to
# 00:03:06 => 00:00:29

# 186-29=157s

# python3  /Users/jzhang/git-repos/cxbbj2/content/hdjt/scripts/shift_srt.py "/Users/jzhang/git-repos/cxbbj2/content/hdjt/环球系列/新加坡/2015新加坡弘法行 如何从红尘中走向解脱.srt" "/Users/jzhang/git-repos/cxbbj2/content/hdjt/环球系列/新加坡/2015新加坡弘法行 如何从红尘中走向解脱-shift.srt" -157
# python3  /Users/jzhang/git-repos/cxbbj2/content/hdjt/scripts/shift_srt.py "/Users/jzhang/git-repos/cxbbj2/content/hdjt/环球系列/马来西亚/2015马来西亚系列讲座 死亡的真相.srt" "/Users/jzhang/git-repos/cxbbj2/content/hdjt/环球系列/马来西亚/2015马来西亚系列讲座 死亡的真相-shift.srt" -6
# python3  /Users/jzhang/git-repos/cxbbj2/content/hdjt/scripts/shift_srt.py "/Users/jzhang/git-repos/cxbbj2/content/hdjt/环球系列/马来西亚/2016马来西亚弘法行 三殊胜.srt" "/Users/jzhang/git-repos/cxbbj2/content/hdjt/环球系列/马来西亚/2016马来西亚弘法行 三殊胜-shift.srt" -84
# python3  /Users/jzhang/git-repos/cxbbj2/content/hdjt/scripts/shift_srt.py "/Users/jzhang/git-repos/cxbbj2/content/hdjt/环球系列/马来西亚/2016马来西亚弘法行 菩提心的修法.srt" "/Users/jzhang/git-repos/cxbbj2/content/hdjt/环球系列/马来西亚/2016马来西亚弘法行 菩提心的修法-shift.srt" -6
# todo ”/Users/jzhang/git-repos/cxbbj2/content/hdjt/环球系列/马来西亚/2017马来西亚弘法行 生活中的大乘佛教.md“

import re
import sys
from datetime import timedelta

TIME_PATTERN = re.compile(
    r"(\d{2}):(\d{2}):(\d{2}),(\d{3})"
)

def parse_time(match):
    h, m, s, ms = map(int, match.groups())
    return timedelta(hours=h, minutes=m, seconds=s, milliseconds=ms)

def format_time(td):
    total_ms = int(td.total_seconds() * 1000)
    if total_ms < 0:
        total_ms = 0

    h, rem = divmod(total_ms, 3600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)

    return f"{h:02}:{m:02}:{s:02},{ms:03}"

def shift_srt(input_path, output_path, shift_seconds):
    shift = timedelta(seconds=shift_seconds)

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    def replace(match):
        t = parse_time(match) + shift
        return format_time(t)

    shifted = TIME_PATTERN.sub(replace, content)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(shifted)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python shift_srt.py input.srt output.srt seconds")
        print("Example: python shift_srt.py in.srt out.srt 15")
        sys.exit(1)

    input_srt = sys.argv[1]
    output_srt = sys.argv[2]
    seconds = float(sys.argv[3])

    shift_srt(input_srt, output_srt, seconds)
