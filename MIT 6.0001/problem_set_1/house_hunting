class Solution() :
    def house_hunting(self) :
        annual_salary = float(input("Enter your annual salary: "))
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
        total_cost = float(input("Enter the cost of your dream home: "))
        portion_down_payment = 0.25
        current_savings = 0
        monthly_salary = annual_salary / 12
        months = 0
        while current_savings < (total_cost * portion_down_payment) :
            months += 1
            current_savings += current_savings * 0.04 / 12
            current_savings += monthly_salary * portion_saved
        print(f'Number of months: {months}')
    

my_sol = Solution()
my_sol.house_hunting()