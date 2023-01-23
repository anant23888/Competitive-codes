#include <GL/glew.h>
#include <GL/glut.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glext.h>
#include <iostream>
#include <string>

#include <stdlib.h>
#include <math.h>

using namespace std;


void setPixel(int x, int y)
{
    glColor3f(1.0, 1.5, 0.5); //Set pixel to black  
    glBegin(GL_POINTS);
    glVertex2i(x, y); //Set pixel coordinates 
    glEnd();
    glFlush(); //Render pixel
}

void bresenham(void){
    
    int x0=30;
    int y0=10;
    int xEnd=150,yEnd=120;

    int dx=fabs(xEnd-x0);int dy=fabs(yEnd-y0);
    int p=2*dy-dx;
    int twoDy=2*dy, twoDyMinusDx=2*(dy-dx);
    int x, y;

    if(x0>xEnd){
        x=xEnd;
        y=yEnd;
        xEnd=x0;
    }
    else{
        x=x0;
        y=y0;
    }
    SetPixel(x,y);

    while(x<xEnd){
    x++;
    if(p<0){
        p+=twoDy;
    }
    else{
        y++;
        p+=twoDyMinusDx;
    }
    SetPixel(x,y);
    }
}

void init (void)
{
    glClearColor(1.0, 2.0, 1.5, 0.5);

    glMatrixMode(GL_PROJECTION);
    gluOrtho2D (0.0, 200.0, 0.0, 150.0);
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(600,500);
    glutInitWindowPosition(60,120);
    glutCreateWindow("Basic OpenGL Program");
    init();
    glutDisplayFunc(bresenham);
    glutMainLoop();

    return 0;
}