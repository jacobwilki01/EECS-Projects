def rec_elim(ups,downs,totals):
    round_count = 0
    if (len(ups) + len(downs)) == 1:
        return round_count
    else:
        if len(downs) == 0:
            if len(ups) % 2 != 0:
                is_odd = True
            else:
                is_odd = False
            downs = ups // 2
            ups //= 2
            if is_odd:
                ups += 1
        

def main():
    downs, totals = 0, []
    ups = int(input("How many entries?: "))
    rec_elim(ups,downs,totals)

if __name__ == "__main__":
    main()