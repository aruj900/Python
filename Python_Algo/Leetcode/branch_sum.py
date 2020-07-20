t={
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None
            }
        },
        "right": None
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": None,
                "right": None
            },
            "right": {
                "value": -3,
                "left": None,
                "right": None
            }
        }
    }
}
s = 7

def hasPathWithGivenSum(t, s):
    if t is None:
        return s == 0    

    return hasPathWithGivenSum(t.left, s - t.value) or hasPathWithGivenSum(t.right, s - t.value)


print(hasPathWithGivenSum(t,s))