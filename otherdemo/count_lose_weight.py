def count_lose_weight(cur,tar,months,avg=False):
    if cur > tar:
        if avg:
            delta = cur - tar
            avg_month_delta = delta/months
            print(f'avg need lose {avg_month_delta/2} kg, {avg_month_delta} jin.')
        else:
            # main lose per month
            if months > 0:
                while months > 0:
                    cur_month_delta = cur * 0.05
                    print(f'Current weight is {cur:.2f} jin, current month should lose weight {cur_month_delta/2:.2f} kg, {cur_month_delta:.2f} jin.')
                    months -= 1
                    cur *= 0.95
                    return count_lose_weight(cur,tar,months,avg=False)
            else:
                return "months may <=0, please check it"

    else:
        return "current weight <= target weight, please check your target"


count_lose_weight(200,10,11)

count_lose_weight(158,88,12)


