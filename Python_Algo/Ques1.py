input = [100, 180, 260, 310, 40, 535,
695]
def maxProfit(input):
        if not input: return 0
        
        high=input[0]
        low=input[0]
        best=[]
        for i in range(len(input)):
            if input[i]>high:
                high=input[i]
                
            if input[i]<low:
                low=input[i]
                high = low
                

        return [low,high]

print(maxProfit(input))