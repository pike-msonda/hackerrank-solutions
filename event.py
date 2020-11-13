arrival =  [978, 409, 229, 934, 299, 982, 636, 14, 866, 815, 64, 537, 426, 670, 116, 95, 630]
duration =  [502, 518, 196, 106, 405, 452, 299, 189, 124, 506, 883, 753, 567, 717, 338, 439, 145]

# arrival = [150, 580, 822, 968, 673, 394, 337, 486, 746, 229, 92, 195, 358, 2]
# duration = [154, 709, 945, 669, 491, 125, 197, 531, 904, 723, 667, 550, 25, 802]

def maxEvents(arrival, duration):
    eventBag = []
    timeValues = [arrival, duration]
    arrival, duration = zip(*sorted(zip(arrival, duration)))
    maxArrivalTime = [ x + y for x, y in zip(arrival, duration)]
    # import pdb; pdb.set_trace()
    print(arrival)
    print(duration)
    print(maxArrivalTime)
    for index in range (len(arrival)):

        if len(eventBag) == 0:
            idx = get_fastest_co(maxArrivalTime, index)
            eventBag.append([arrival[idx], duration[idx]])
        else:
            verd = timeSlotAvailable(eventBag, arrival[index])
            if (verd):
                # add next event
                add_index = get_fastest_co(maxArrivalTime, index)
                eventBag.append([arrival[add_index], duration[add_index]])
    return len(eventBag)

def get_fastest_co(time_list, curr):
    return time_list.index(min(time_list[curr:]))

def timeSlotAvailable(eventBag, arrivaltime):
        arrvTimeDiff = arrivaltime - eventBag[len(eventBag) - 1][0]
        return arrivaltime > eventBag[len(eventBag) - 1][0] and arrvTimeDiff >= eventBag[len(eventBag) - 1][-1]



if __name__ == "__main__":
    print(maxEvents(arrival, duration))