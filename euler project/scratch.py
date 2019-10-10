import time
from functools import reduce
start = time. time()

def num1(arr):
    sum = 0
    for i in range(2,arr):
        if i%3  == 0 or i%5 == 0:
            sum += i
    print(sum)
#num1(1000)


def num2():
    a = 1
    b = 2
    sum =  2
    while b < 4*10**6:
        a , b = b , a + b
        if b % 2 == 0:
            sum += b
    print(sum)

#num2()

def num3(num): #incorrect(random picked number)
    max = 2
    for i in range(2,num):
        if num % i == 0:
            print(num/i)
#num3(600851475143)


def palindrome(num):
    return str(num) == str(num)[::-1]
def num4():
    max = 1
    for i in range(999,100,-1):
        for j in range(i,100,-1):
            print(i,j , i*j )
            cur = i*j
            if  palindrome(cur) and cur > max:

                max = i*j
    return  max
#print(num4())

def num5(num):
    i = 2520  # Делимость на 20
    c = False
    r = (3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19)
    while c is False:
        str(i)
        for j in r:
            if i % j == 0:
                c = True
                continue
            else:
                c = False
                break
        i += 20  # Только четные

    print(i - 20)
#num5(20)

def num6():
    sum_sqrt = 0
    sum = 0
    for i in range(1,101):
        sum_sqrt += i**2
        sum += i
    print(sum , sum_sqrt)
    return sum**2 - sum_sqrt
#print(num6())


def num7():
    arr = [2,3,5,7]
    flag = 4
    start = 7
    while flag != 10001:
        for i in arr:
            if start % i == 0 or i > start**2:
                break
            elif i == arr[-1] :
                flag += 1
                arr.append(start)
        start += 1
    return start

def is_prime(num): #prime check for number
    for i in range(3,int(num**0.5)+1,2):
        if  num % i == 0 :
            return False
    return True
def num7_opt(flag):
    i = 4
    start = 9
    while i != flag:
        if is_prime(start):
            i += 1
        start += 2
    return start-2
#print(num7_opt(10001))



num_str=('''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450''')

def num8(num_str):
    max = 0
    num_str.replace('0','')
    num_arr = list(num_str.replace('\n',''))
    for i in range(0,len(num_arr)-13):
        multi = 1
        for j in range(13):
            print(i , j)
            multi *= int(num_arr[i+j])
        if multi > max:
            max = multi
            print(i)
    print(max)
#num8(num_str)



def num9():
    start = 150
    for a in range(start+1,301):
        for b in range(a+1,401):
            c = a**2+b**2
            if (c)**0.5 % 1 == 0 and a + b + c**0.5 == 1000:
                return a * b*c**0.5

#print(int(num9()))



def num10():
    sum = 2
    end = 2*10**6
    for i in range(3,end,2):
        if is_prime(i):
            sum += i
    return sum

#print(num10())

def num10_opt(): # with Sieve of Eratosthenes usage
    end = 2*10**6
    arr = list(range(end+1))
    arr[1] = 0
    for i in arr:
        if i > 1:
            for j in range(i+i,len(arr),i):
                arr[j]=0
    return  sum(arr)


#print(num10_opt())
arr_num11 =('''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48''')

def num11(): # EZ
    arr = [list(map(int,i.split())) for i in arr_num11.split("\n")] # :3
    print(arr)
    max = 0
    temp = 0
    for i in range(20):
        for j in range(17):
            temp = arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3]
            if temp>max :
                max = temp
    for i in range(17):
        for j in range(20):
            temp = arr[i][j] * arr[i-1][j] * arr[i-2][j] * arr[i-3][j]
            if temp>max :
                max = temp
    for i in range(17):
        for j in range(17):
            temp = arr[i][j] * arr[i+1][j + 1] * arr[i+1][j + 2] * arr[i+1][j + 3]
            if temp > max:
                max = temp
    for i in range(4,20):
        for j in range(17):
            temp = arr[i][j] * arr[i - 1][j+1] * arr[i - 2][j + 2] * arr[i - 3][j+3]
            if temp > max:
                max = temp
    print(max)



#num11()
def num12(num):
    dividers = set()
    opers = []
    sum = 0
    i = 1
    while len(dividers) < num:
        dividers.clear()
        sum +=i
        opers.append(i)
        for j in opers:
            if sum%j == 0 and j < sum**0.5 + 1:
                dividers.update([int(j), int((sum/j)) , int(sum)])
            else:
                break
            print(sum, dividers)
        i += 1
    return sum

def dividers(n):
    div = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            div += 1
    return div * 2
def num12_opt():
    n = 1
    while True:
        if n % 2 == 0:
            div = dividers(n / 2) * dividers(n + 1)
        else:
            div = dividers((n+1)/2)*dividers(n)
        print(div)
        if div > 5:
            break
        else:
            n += 1
    return n*(n+1)/2
    return n*(n+1)/2


#print(num12_opt())


num13_arr = '''
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690'''


def num13():
    arr = num13_arr.split()
    j = 0
    sum = 0
    arr_i = 0
    while True:
        for i in range(100):
            arr_i += int(arr[i][j])
        if sum < 10**20:
            sum = sum*10 + arr_i
        elif sum == 0:
            sum = arr_i
        else:
            sum = sum//(10**11)
            break
        arr_i = 0
        j += 1
    return sum


def num13_straight():
    arr = num13_arr.split()
    sum = 0
    for i in arr:
        print(i)
        sum += int(i)
    print(sum)
    print(str(sum)[0:10])
#num13_straight()
#print(num13())


def num14():
    collatz_dict = {1:1}
    count = 0
    for i in range(1,1000000,2):
        sum = i
        while not sum in collatz_dict:
            if sum % 2 == 0:
                sum /= 2
            else:
                sum = sum*3 + 1
            count += 1
        collatz_dict[i] = collatz_dict[sum] + count
        count = 0
    print(collatz_dict[837799])
    return max(collatz_dict, key= collatz_dict.get)
#print(num14())

#def num15()  #SMOrc

def num16():
    sum = 0
    times = str(2**1000)
    print(times)
    for i in range(len(times)):
        sum += int(times[i])
    return  sum
#print(num16())

def num17(): # incorrect
    num_name = {0:0,00:0,1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,
                50:5,60:5,70:7,80:6,90:6}
    sum = 0
    for i in range(1000):
        sum_i = sum
        if i >= 100:
            if i % 100 != 0:
                sum += num_name[i//100] + 10 + num_name[(i%100)//10*10]+ num_name[i%10]
            elif i % 100 == 0:
                #print(1)
                sum += num_name[i // 100 ] + 7
                #print(sum-sum_i)
        elif i >= 20:
            sum += num_name[i // 10 * 10] + num_name[i % 10]
        else:
            #print(2)
            sum += num_name[i]
            #print(i, ' ',sum - sum_i)
        #print(i, ' ', sum -sum_i)
    return sum + 47

#print(num17())

num18_arr='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
def num18():
    arr = num18_arr.split('\n')
    new_arr = []
    temp_arr = []
    for i in range(len(arr)-1):
        new_arr.append([])
        temp_arr.append([])
    arr = arr[0:-1]
    for i in range(len(arr)):
        for j in arr[i].split():
            new_arr[i].append(int(j))
    print(new_arr)
    temp_arr[0] = [75]
    for i in range(1,len(new_arr)):
        pos = 0
        j = 0
        while j < len(temp_arr[i-1]):                                  #for j in range()):
            if j == 0:
                print("START")
                temp_arr[i].append(new_arr[i][pos] + temp_arr[i - 1][j])
                temp_arr[i].append(new_arr[i][pos+1] + temp_arr[i - 1][j])
                pos += 1
                j+=1
            elif j == len(temp_arr[i-1])-1:
                print("END")
                temp_arr[i].append(new_arr[i][len(new_arr[i])-2] + temp_arr[i - 1][j])
                temp_arr[i].append(new_arr[i][len(new_arr[i])-1] + temp_arr[i - 1][j])
                pos = 0
                j+=1
            else:
                print("MID")
                print(len(new_arr[i]), pos, len(temp_arr[i-1])-1,j)
                temp_arr[i].append(new_arr[i][pos] + temp_arr[i - 1][j])
                temp_arr[i].append(new_arr[i][pos + 1] + temp_arr[i - 1][j])
                j += 1
                temp_arr[i].append(new_arr[i][pos] + temp_arr[i - 1][j])
                temp_arr[i].append(new_arr[i][pos + 1] + temp_arr[i - 1][j])
                pos += 1
                j+=1
            print(pos, new_arr[i],temp_arr[i])
        pos = 0
        print(new_arr,"\n\\" , temp_arr)

def num18_2():
    arr = [i.split() for i in num18_arr.split('\n')]
    arr = arr[0:-1]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = int(arr[i][j])
    print(arr)
    for i in range(len(arr)-2,-1,-1):
        for j in range(len(arr[i])):
            if arr[i+1][j]+arr[i][j] > arr[i+1][j+1]+arr[i][j]:
                arr[i][j] = arr[i + 1][j]+arr[i][j]
            else:
                arr[i][j] = arr[i + 1][j + 1]+arr[i][j]

    print(arr)
#num18_2()

def num19():
    def_year = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = 1
    mondays = 0
    for y in range(1901,2001):
        if y % 4 != 0 and y % 100 != 0:
            current_year = def_year
        else:
            current_year = leap_year
        for i in range(len(current_year)):
            for j in range(current_year[i]):
                day += 1
                if day%7==0 and j == 0:
                    mondays +=1
                    print(y,i,j)

    print(mondays)
#num19()


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def num20():
    print(sum([int(i) for i in list(str(factorial(100)))]))
#num20()


def num20_lambda():

    print(sum([int(i) for i in list(str(reduce(lambda x, y: x * y, range(1, 101))))]))
    print(sum(map(int,list(str(reduce(lambda x,y:x*y,range(1,101)))))))
#num20_lambda()


def dividers_sum(n):
    sum = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 :
            if i*i != n:
                sum += i + n/i
            else:
                sum += i
    return int(sum)+1
def num21():
    sum = 0
    dividers_dict = {}
    for i in range(2,10000):
        c = dividers_sum(i)
        dividers_dict[i] = c
        if c in dividers_dict and dividers_dict[c] == i and i != c:
            sum += c + i
            print(i,dividers_dict[i],c,dividers_dict[c])
    print(sum)

#num21()

def num22():
    with open("p022_names.txt") as text:
        names = sorted(text.read().replace('"','').split(','))
        n = 0
        it = 0
        for i in names:
            it+=1
            temp = 0
            for j in i:
                temp += ord(j)-64
            n += temp*it
    print(n)

def num22_2():
    print(sum(list(map(lambda x:(x[0]+1)*sum([ord(i)-64 for i in x[1]]),enumerate(sorted(open("p022_names.txt").read().replace('"','').split(',')))))))


#num22()
#num22_2()

'''
list(map(lambda x: print(x[0],x[1]),enumerate([int(i+1) for i in range(10)]))) ^_^
'''

def num23(): #too slow and weird way to do this tusk
    n = [i for i in range(28123)]
    p = 0
    over_cup = []
    for i in range(2,28123):
        if i < dividers_sum(i):
            over_cup.append(i)
            for j in range(len(over_cup)):
                try:
                    n[over_cup[j]+over_cup[-1]] = 0
                except IndexError:
                    break
    print(sum(n))
    '''print(over_cup)
    for i in range(len(over_cup)):
        for j in range(i,len(over_cup)):
            if over_cup[i]+over_cup[j] < 28123:
                n[over_cup[i]+over_cup[j]] = 0
            else:
                break
    print(sum(n))'''
#num23()

def fibonacci(n):
    if n <= 2:
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
def num25():
    a = 1
    b = 1
    i = 2
    while b < 10**999:
        b,a = b+a , b
        i+=1
    print(i,len(list(str(b))),b)

#num25() #derp



def num26():
    max = 6
    for i in range(11,1001):
        temp = str(1/i)[3:]
        for j in range(len(temp)//2):
            for b in range(j):
                c = temp.count(temp[b:j])
                if c>1 and j-b>max:
                    max = j
                    print(i)
    print(max)


#num26()
def is_simple(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return  True

def num27():
     for i in range(1000,500,-1):
         if is_simple(i):
             pass

num27()

end = time.time()
print(end - start)
