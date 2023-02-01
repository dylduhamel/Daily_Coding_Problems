# Important
# O(N*K) where N is the number of "\n" in the string and K is the "\t" in the sub-string.
def directoryLength(path):
    if not path:
        return

    level = {-1: 0}
    maxLen = 0

    files = path.split("\n")

    for line in files:
        # gives the number of \t (tabs, which == the depth)
        depth = line.count("\t")
        # subtract depth because we want to have \ but not t (\t)
        level[depth] = len(line) - depth + level[depth - 1]

        if '.' in line:
            maxLen = max(maxLen, level[depth] + depth)
        
    return maxLen

testString = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

print(directoryLength(testString))