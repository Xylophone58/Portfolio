//Zach Mitchell 700726936

#include <stdio.h>

double add(double x, double y)
{
    double result = x + y;
    printf("%.4lf + %.4lf = %.4lf\n", x, y, result);
    return result;
}

double sub(double x, double y)
{
    double result = x - y;
    printf("%.4lf - %.4lf = %.4lf\n", x, y, result);
    return result;
}

double mul(double x, double y)
{
    double result = x * y;
    printf("%.4lf * %.4lf = %.4lf\n", x, y, result);
    return result;
}

double div(double x, double y)
{
    
    double result = x / y;
    printf("%.4lf / %.4lf = %.4lf\n", x, y, result);
    return result;
    
}

struct cmd
{
	char   cmd_name;
	double (*cmd_pointer)(double, double);
}; 

struct cmd calc_cmds[] =
	{{'+',	add   },
	 {'-',	sub   },
	 {'*',	mul   },
	 {'/',	div   },
	};

int main()
{
	double operand1, operand2;
	char operation;
    while( scanf("%lf %c %lf",&operand1, &operation,&operand2) == 3)
    {
        for (int i = 0; i < sizeof(calc_cmds) / sizeof(calc_cmds[0]); ++i)
        {
            if (calc_cmds[i].cmd_name == operation)
            {
                calc_cmds[i].cmd_pointer(operand1, operand2);
                break;
            }
        }
    }
}