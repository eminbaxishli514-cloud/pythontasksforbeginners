import pandas as pd
import numpy as np
#task 1
"""def count_password_strength(password):
    special_chars = "!@#$%^&*?"
    score = 0
    uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
    lowercase = "qwertyuiopasdfghjklzxcvbnm"
    for i in password:
        if i in special_chars:
            score+=4
        elif i in "0123456789":
            score+=3
        elif i in uppercase:
            score+=2
        elif i in lowercase:
            score+=1
    return score

password= "Salam1234"
print(count_password_strength(password))"""
#task 2
"""def parse_log_line(line):
    list = line.split(":")
    line_part1 = list[0]
    line_part2 = list[1]
    list2 = line_part1.split()
    line_part1_1 = list2[0]
    line_part1_2 = list2[1]
    x = ""
    for i in line_part1_1:
        if i != "[" and i!= "]":
            x +=i
    return f'("{x}","{line_part1_2}","{line_part2}")'


line = "[2025-02-18] root:LOGIN"
print(parse_log_line(line))"""
#task 3
"""def find_anomaly(nums):
    for i in range(0,len(nums)-1):
        if nums[i]>nums[i+1]:
            return i+1
            break


nums = [1,2,3,4,1,2,3]
print(find_anomaly(nums))"""
#task 4
"""def ip_status(allowed, blocked):
    allowed = ["10.0.0.1", "10.0.0.5", "192.168.1.10"]
    blocked = ["10.0.0.5", "172.16.0.1"]
    allowed_1 = []
    result = ""
    for i in allowed:
        if i not in blocked:
            allowed_1.append(i)
    for i in allowed_1:
        result += f"({i},ALLOWED)\n"
    for i in blocked:
        result += f"({i},BLOCKED)\n"
    return result

allowed = ["10.0.0.1", "10.0.0.5", "192.168.1.10"]
blocked = ["10.0.0.5", "172.16.0.1"]
print(ip_status(allowed,blocked))"""
#task 5
"""def count_digits_recursive(n):
    count = 0
    while n > 0:
        n = n//10
        count+=1
    return count

n = 1234
print(count_digits_recursive(n))"""
#task 6
"""def has_permission(acl, user, permission):
    if user not in acl:
        return False
    for key in acl:
        if key ==user:
            k = 0
            for value in acl[key]:
                if value == permission:
                    k = True
                    return k
            if k ==0:
                return False

acl = {

    "alice": ["read", "write"],
    
    "bob": ["read"],
    
    "root": ["read", "write", "delete"]
    
}
print(has_permission(acl, "root", "delete"))"""
#task 7
"""class Incident:
    def __init__(self,message,severity,resolved=False):
        self.message = message
        self.severity = severity
        self.resolved = resolved

    def is_critical(self):
        if self.severity >= 8:
            return True
        else:
            return False
    def resolve(self):
        self.resolved = True
    def summary(self):
        if self.resolved == True:
            if self.severity >= 8:
                return f"CRITICAL - RESOLVED"
            else:
                return f"NORMAL - Resolved"
        else:
            if self.severity >= 8:
                return f"Critical"
            else:
                return f"Normal"
k = Incident("Brute force", 9)
k.resolve()
print(k.summary())"""
#task 8
"""array = np.random.randint(10,35,size=(5,5))
row_mean = np.mean(array,axis = 1)
maximum_value = np.max(array)
sum_of_diagonal = 0
for i in range(0,len(array)):
    for j in range(len(array)):
        if i == j:
            sum_of_diagonal += array[i,j]

print(array)
print(row_mean)
print(maximum_value)
print(sum_of_diagonal)
print(array.shape)"""
#task 9
"""df = pd.DataFrame({
    "User": ["Leyla", "Samir", "Emin"],
    "LoginCount": [5, 3, 1],
    "FailedAttempts": [3, 2, 0]
})
df["Riskscore"] = df["FailedAttempts"] * 2 + df["LoginCount"] * 0.5
max_risk = df["Riskscore"].max()
risky_user = df.loc[df["Riskscore"] == max_risk]
print("Top risk")
print(risky_user)"""
#task 10
"""def validate_port(port):
    assert type(port) is int, "The port number must be an integer"
    if not (1 <= port <= 65535):
        raise ValueError("The port number must be between 1 and 65535")

    return "VALID"

try:
    print(f"Result : {validate_port(443)}")
except Exception as e:
    print("Test 1 error: ",e)
try:
    print("Test 1:", validate_port(8080))
except Exception as e:
    print("Test 1 Error:", e)
try:
    print("Test 2:", validate_port("80"))
except Exception as e:
    print("Test 2 Error:", e)
try:
    print("Test 3:", validate_port(70000))
except Exception as e:
    print("Test 3 Error:", e)"""




































    









    





















            
