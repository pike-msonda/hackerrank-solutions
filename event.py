arrival =  [978, 409, 229, 934, 299, 982, 636, 14, 866, 815, 64, 537, 426, 670, 116, 95, 630]
duration =  [502, 518, 196, 106, 405, 452, 299, 189, 124, 506, 883, 753, 567, 717, 338, 439, 145]

# duration =[819,397,693,816,992,34,670,398,554,548,826,211,663,212,809,378,762,626,336,869,996,777,768]
# arrival = [1,1,1,1,4]
# duration =[10,3,6,4,2]

def maxEvents(arrival, duration):
    eventBag = []
    timeValues = [arrival, duration]
    arrival, duration = zip(*sorted(zip(arrival, duration)))
    maxArrivalTime = [ x + y for x, y in zip(arrival, duration)]
    import pdb; pdb.set_trace()
    for index, arv in enumerate(arrival):
        if len(eventBag) == 0:
            eventBag.append([arv, duration[index]])
        else:
            verd = timeSlotAvailable(eventBag, arv)
            if (verd and  ((arv + duration[index]) < maxArrivalTime)):
                
                eventBag.append([arv, duration[index]])
    return len(eventBag)


def timeSlotAvailable(eventBag, arrivaltime):
        arrvTimeDiff = arrivaltime - eventBag[len(eventBag) - 1][0]
        return arrivaltime > eventBag[len(eventBag) - 1][0] and arrvTimeDiff >= eventBag[len(eventBag) - 1][-1]



if __name__ == "__main__":
    print(maxEvents(arrival, duration))