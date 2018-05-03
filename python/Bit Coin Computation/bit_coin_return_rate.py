import math
import requests

RATE = [0.31, 0.29, 0.27, 0.25, 0.23]
POWER = [ 700, 1400, 2800, 5600]
BIT_COIN_PER_DAY = 7.40e-6
BIT_COIN_COST = 4.88e-4
MIN_NUM_BIT_COIN_PURCHASE = 20
MONEY_PER_DAY_PER_BIT_COIN = 4.7e-3
CONVERSION_PER_BIT_COIN = 708

CUMULATIVE_BUY = True
FREE_INITIAL_POWER = 15
AMOUNT_TO_INVEST_EVERY_MONTH = 0

start_money = 25
NUM_YEARS = 1
NUM_DAYS = int(math.floor(365 * NUM_YEARS))

def get_bit_coin_conversion_rate():
    response = requests.get('https://chain.so/api/v2/get_price/BTC/USD',verify=True)

    response = response.json()['data']['prices']
    cumulative = 0
    for i in response:
        cumulative += float(i['price'])
    return cumulative / len(i)


def get_rate(target_power):
    for i in range(0, len(POWER)):
        if target_power < POWER[i]:
            return RATE[i]
    return RATE[-1]

def num_bit_coin_to_buy(money, rate):
    return math.floor(money / rate)

def bit_coin_reduction_compute(num_buy, rate):
    return (num_buy * rate) / CONVERSION_PER_BIT_COIN

def buy_bit_coin_from_money(money):
    bc = money / CONVERSION_PER_BIT_COIN
    power, bc_reduction = buy_bit_coin(bc)
    return power, (bc-bc_reduction)

def buy_bit_coin(bit_coin):
    money = bit_coin * CONVERSION_PER_BIT_COIN
    for i in reversed(POWER):
        rate = RATE[POWER.index(i) + 1]
        if money > i * rate:
            num_bc_to_buy = num_bit_coin_to_buy(money, rate)
            bit_coin_reduction = bit_coin_reduction_compute(num_bc_to_buy, rate)
            return num_bc_to_buy, bit_coin_reduction
    rate = RATE[0]
    if money > rate * MIN_NUM_BIT_COIN_PURCHASE:
        num_bc_to_buy = num_bit_coin_to_buy(money, rate)
        bit_coin_reduction = bit_coin_reduction_compute(num_bc_to_buy, rate)
        return num_bc_to_buy, bit_coin_reduction
    return 0, 0

def print_stat(start_power, bc, power, days, number_of_days):
    print '$ / BC: %f' % (CONVERSION_PER_BIT_COIN)
    print 'power (KH/s) at start:', start_power
    if number_of_days:
        print 'number of days to break even in one day of mining\t', number_of_days
    print 'After', days, 'days:'
    print 'end period power (KH/s): %10s' % (power)
    print 'money converted from BC ($): %10s' % (cumulative_bit_coin * CONVERSION_PER_BIT_COIN)
    print '$/day %10.2f' % (power * BIT_COIN_PER_DAY * CONVERSION_PER_BIT_COIN)
    print 'monthly income: %10.2f' % (power * BIT_COIN_PER_DAY * CONVERSION_PER_BIT_COIN * 30)


if __name__ == '__main__':
    CONVERSION_PER_BIT_COIN = get_bit_coin_conversion_rate()
    power, cumulative_bit_coin = buy_bit_coin_from_money(start_money)
    power += FREE_INITIAL_POWER

    break_even = False
    start_power = power
    total_invest = start_money
    number_of_days = None

    print '%20s\t%20s\t%20s\t%20s' % ('buy @ day', 'prev power', 'power to buy', 'new power')
    for i in range(NUM_DAYS):
        if i%30 == 0 and i > 0:
            power_to_buy, bit_coin_left = buy_bit_coin_from_money(AMOUNT_TO_INVEST_EVERY_MONTH)
            power += power_to_buy
            cumulative_bit_coin += bit_coin_left
            total_invest += AMOUNT_TO_INVEST_EVERY_MONTH
        cumulative_bit_coin += power * BIT_COIN_PER_DAY
        if CUMULATIVE_BUY:
            money = cumulative_bit_coin * CONVERSION_PER_BIT_COIN
            if money >= total_invest and not break_even:
                number_of_days = i + 1
                break_even = True
            power_to_buy, bc_reduction = buy_bit_coin(cumulative_bit_coin)
            if power_to_buy > 0:
                prev_power = power
                power += power_to_buy
                cumulative_bit_coin -= bc_reduction
                print '%20s\t%20s\t%20s\t%20s' % (i + 1, prev_power, power_to_buy, power)
    print
    print_stat(start_power, cumulative_bit_coin, power, NUM_DAYS, number_of_days)
    print 'total invested: ', total_invest
