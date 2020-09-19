#include<iostream>
#include<cmath>

class Function {
    public:
        virtual double operator() (double x);
};

double Function::operator() (double x) {
    return 1.0;
}

class Sinus : public Function
{
    public:
        virtual double operator() (double x);
};

double Sinus :: operator() (double x) {
    return std::sin(x);
}

double ableitung (Function& f, double x, double dx) {
    return (f(x + dx) - f(x))/dx;
}

int main()
{
    Sinus sin; double x = 3.14; double dx = 1e-6;
    std::cout << ableitung(sin, x, dx);
    return 0;
}