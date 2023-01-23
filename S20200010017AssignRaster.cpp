
#include <GL/glew.h>
#include <GL/glut.h>
#include<bits/stdc++.h>
#include<stdlib.h>
#include<math.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glext.h>
#include <iostream>
#include <string>
using namespace std;
void setPixel(int x, int y)
{
    glColor3f(1.5, 0.7, 2.0); 
    glBegin(GL_POINTS);
    glVertex2i(x, y); 
    glEnd();
    glFlush(); 
}
int arr[3][4]={{20,5,160,100},{20,5,100,20},{100,20,160,100}};
void line(int x0,int y0,int xEnd,int yEnd){
    int dx=fabs(xEnd-x0),dy=fabs(yEnd-y0);
    int twoDy=2*dy,twodyMinus=2*(dy-dx);
    int p=2*dy-dx;
    int x,y;
    if(x0>xEnd){
        x=xEnd;
        y=yEnd;
        xEnd=x0;
    }
    else{
        x=x0;
        y=y0;
    }
    setPixel(x,y);
    while (x<xEnd)
    {
        x++;
        if(p<0){
            p+=twoDy;
        }
        else{
            y++;
            p+=twodyMinus;
        }
        setPixel(x,y);
    }
}
void triangle(int x,int y){
    float w_1=arr[0][0]*(arr[1][3]-arr[0][1])+(y-arr[0][1])*(arr[1][2]-arr[0][0])-x*(arr[1][3]-arr[0][1]);
    float f=(arr[0][3]-arr[0][1])*(arr[1][2]-arr[0][0])-(arr[0][2]-arr[0][0])*(arr[1][3]-arr[0][1]);
    w_1=w_1/f;
    float w_2=y-arr[0][1]-w_1*(arr[0][3]-arr[0][1]);
    w_2=w_2/(arr[1][3]-arr[0][1]);
    if(w_1>=0.0 && w_2>=0.0){
        if(w_1+w_2<=1.0){
            setPixel(x,y);
        }
    }
}
void algorithmBresen(){
    line(20,5,150,90);
}
void bresLine(){
    line(arr[0][0],arr[0][1],arr[0][2],arr[0][3]);
    line(arr[1][0],arr[1][1],arr[1][2],arr[1][3]);
    line(arr[2][0],arr[2][1],arr[2][2],arr[2][3]);
    for(int i=arr[0][0];i<=arr[0][2];i++){
        for(int j=arr[0][1];j<=arr[0][3];j++){
            triangle(i,j);
        }
    }
}
void init()
{
   glClearColor(1.0, 1.0, 1.0, 1.0);
    glMatrixMode(GL_PROJECTION);
    gluOrtho2D (0.0, 200.0, 0.0, 150.0);

}
void displayTriangle() 
{
	glClearColor(0, 0, 1, 1);
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_TRIANGLES);
	glShadeModel(GL_FLAT);
	glVertex2f(-0.75, -0.75);
	glVertex2f(0.75, -0.75);
	glVertex2f(0, 0.75);
	glEnd();
	glutSwapBuffers();
}
int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(400, 300);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Bresenham Line");
    glewInit();
    init();
    glutDisplayFunc(algorithmBresen);


    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(400, 300);
    glutInitWindowPosition(200, 500);
    glutCreateWindow("Coverage Triangle");
    glewInit();
    init();
    glutDisplayFunc(bresLine);
    


    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("Sample Triangle  coverage");
	glutDisplayFunc(displayTriangle);
    
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE);
	glEnable(GL_MULTISAMPLE);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(400, 700);
	glutCreateWindow("Anti Aliasing using Super Sampling for Triangle");
	glutDisplayFunc(displayTriangle);
    glutMainLoop();
    return 0;
}