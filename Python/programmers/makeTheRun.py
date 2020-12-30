import collections
def makeTheRun(participant, completion):
    result = []
    c1 = collections.Counter(participant)
    c2 = collections.Counter(completion)
    print(c1, c2)
    a = list((c1-c2).elements())
    print(a[0])
makeTheRun(["leo", "kiki", "eden"],["eden", "kiki"])