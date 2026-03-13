#include<stdio.h>
#include<stdlib.h>
#include<time.h>

/* generate the random numbers*/
void generater_random(int a[], int n){
    for(int i = 0; i<n; i++)
        a[i]= rand() %1000;
}

/*bubble sort*/
void bubble_sort(int a[], int n)
{
    int temp;
    for(int i= 0; i<n-1;i++){
        for (int j = 0;j<n-1;j++){
            if(a[j]>a[j+1]){
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
}
int main()
{
    int a[10000];
    clock_t start,end;
    double time_taken;
    double theoretical_time;
    FILE *fp;

    srand(time(NULL));
    fp = fopen("bubble_time.txt","w");  
    for(int n = 100; n <=10000; n+=100)
    {
        generater_random(a,n);
        start=clock();
        bubble_sort(a,n);
        end=clock();
        time_taken=(double)(end - start)/CLOCKS_PER_SEC;
        theoretical_time=(double)(n*n)*1e-8;
        fprintf(fp,"%d %lf %lf\n",n,time_taken,theoretical_time);
    }

    fclose(fp);
    FILE *gnuplotPipe = popen("gnuplot -persistent", "w");

    fprintf(gnuplotPipe,"set title 'bubble sort time efficiency'\n");
    fprintf(gnuplotPipe,"set xlabel 'Input Size'\n");
    fprintf(gnuplotPipe,"set ylabel 'Time (seconds)'\n");

    fprintf(gnuplotPipe, "set grid\n");
    fprintf(gnuplotPipe, "set term png\n");
    
    /* Sets the output format to PNG image */
    
    fprintf(gnuplotPipe, "set output 'bubble_sort_graph.png'\n");
    
    fprintf(gnuplotPipe,
    "plot 'bubble_time.txt' using 1:2 with linespoints title 'Actual Time', "
    "'bubble_time.txt' using 1:3 with lines lw 2 title 'Theoretical O(n^2)'\n");
    
    /* Plots data from the file bubble_time.txt; using 1:2 means column 1 -> X axis,
       column 2 -> Y axis */
    
    /* Plots the theoretical curve from column 3, lines draws a smooth line,
       lw 2 sets the line width */

    fflush(gnuplotPipe);
    pclose(gnuplotPipe);
    return 0;
}