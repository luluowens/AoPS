class Solution() :
    def saving_with_raise(self) :
        annual_salary = float(input("Enter your annual salary: "))
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
        total_cost = float(input("Enter the cost of your dream home: "))
        semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
        portion_down_payment = 0.25
        current_savings = 0
        months = 0
        while current_savings < (total_cost * portion_down_payment) :
            monthly_salary = annual_salary / 12
            months += 1
            current_savings += current_savings * 0.04 / 12
            current_savings += monthly_salary * portion_saved
            if months % 6 == 0 :
                annual_salary *= (semi_annual_raise + 1)
        print(f'Number of months: {months}')

my_sol = Solution()
my_sol.saving_with_raise()
        