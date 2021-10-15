#include<iostream.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
#include<stdlib.h>
#include<time.h>

void swap(char [],char []);

int card1[] = { 20,20 , 50,20 , 50,100 , 20,100 , 20,20 };
int card2[] = { 80,20 , 110,20 , 110,100 , 80,100 , 80,20 };
int card3[] = { 140,20 , 170,20 , 170,100 , 140,100 , 140,20 };

char val[3][2]={ "1" , "2", "3" };

void main()
   {
   clrscr();
   char count[2]="0";
   int swapnum=0;         //for number of times to swap the cards
   int driver,mode;

   driver=DETECT;

   initgraph(&driver , &mode , "c:\tc\bgi");

   setfillstyle(SOLID_FILL,YELLOW);
   fillpoly(5,card1);
   fillpoly(5,card2);
   fillpoly(5,card3);

   settextstyle(GOTHIC_FONT,HORIZ_DIR,6);
   setcolor(BLUE);
   moveto(25,25);
   outtext(val[0]);
   moveto(85,25);
   outtext(val[1]);
   moveto(145,25);
   outtext(val[2]);

   do
      {
      int num=0;
      int choice[2];
      count[0]++;

      delay(1500);

      settextstyle(DEFAULT_FONT,HORIZ_DIR,2);
      moveto(20,150);
      outtext("No. of Times Cards have been swapped:");
      settextstyle(DEFAULT_FONT,HORIZ_DIR,3);
      moveto(20 + swapnum*20,170);
      outtext(count);
      setfillstyle(SOLID_FILL,YELLOW);
      fillpoly(5,card1);
      fillpoly(5,card2);
      fillpoly(5,card3);

      do
	 {
	 randomize();
	 choice[num]= (rand() + num) % 3;

	 switch(choice[num])
	    {
	    case 0:
	       setfillstyle(CLOSE_DOT_FILL,BLUE);
	       fillpoly(5,card1);
	       break;
	    case 1:
	       setfillstyle(CLOSE_DOT_FILL,BLUE);
	       fillpoly(5,card2);
	       break;
	    case 2:
	       setfillstyle(CLOSE_DOT_FILL,BLUE);
	       fillpoly(5,card3);
	       break;
	    }
	 num++;
	 }while(num<2);

      swap(val[(choice[0])],val[(choice[1])]);

      }while(swapnum++ < 6);

   settextstyle(DEFAULT_FONT,HORIZ_DIR,3);
   moveto(20,200);
   outtext("What is card number 2");
   char ans;
   ans=getch();
   if(ans==val[1][0])
      {
      moveto(20,230);
      outtext("HURRAY");
      }
   else
      {
      moveto(20,230);
      outtext("YOU DUMBO");
      }

   getch();
   closegraph();
   }

void swap(char a[], char b[])
   {
   char c;
   c=a[0];
   a[0]=b[0];
   b[0]=c;
   }
