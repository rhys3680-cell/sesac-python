# 20kg >  print(20000)
def luggageCostCalculatr(luggageWeight: int):
    return (
        print("짐에 대한 수수료는 없습니다")
        if luggageWeight < 20
        else print("무거운 짐은 20,000원 내셔야 합니다.")
    )


# number 2
weight = float(input("짐의 무게는 얼마입니까?"))

luggageCostCalculatr(weight)
