class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        
        
        # we can calculate the number of iterations required and store it
        # if next car requires less iterations, then we can "merge" them
        # if next car requires more iterations, then we store it
        # we end up with a monotomically increasing stack
        # result is number of elements in the stack
        
        stack = []
        traffic = [ [car, vel] for car, vel in zip(position, speed) ]
        traffic.sort(reverse = True)
        # print(traffic)
        
        for car, vel in traffic:
            hours = (target - car) / vel
            if stack and stack[-1] >= hours:
                continue
            stack.append(hours)
            
        # print(stack)
        return len(stack)
        
        