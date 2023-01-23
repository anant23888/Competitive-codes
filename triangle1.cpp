#include <GL/glew.h>
#include <GL/glut.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>


int x, xEnd, y, yEnd;

void myInit() 
{
	glClear(GL_COLOR_BUFFER_BIT);
	glClearColor(0.0, 0.0, 0.0, 1.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0, 500, 0, 500);
}

void drawpixel(int x, int y) 
{
	glBegin(GL_POINTS);
	glVertex2i(x, y);
	glEnd();
}

void drawline(int x0, int xEnd, int y0, int yEnd) 
{
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
    drawpixel(x,y);
    while(x<xEnd){
    x++;
    if(p<0){
        drawpixel(x,y);
        p+=twoDy;
    }
    else{
        y++;
        drawpixel(x,y);
        p+=twoDyMinusDx;
    }
    }
}

void myDisplay() 
{
	drawline(x, xEnd, y, yEnd);
	glFlush();
}
void displayTriangle() 
{
	glClearColor(0, 0, 0, 1);
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_TRIANGLES);
	glShadeModel(GL_FLAT);
	glVertex2f(-0.75, -0.75);
	glVertex2f(0.75, -0.75);
	glVertex2f(0, 0.75);
	glEnd();
	glutSwapBuffers();
}

int main(int argc, char** argv) 
{
    printf("Enter first point (x1,y1) : ");
    scanf("%d %d",&x,&y);
    printf("Enter second point (x2,y1) :");
    scanf("%d %d",&xEnd,&yEnd);

	//Question1-Bresemham's Line Drawing.
    glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("Bresenham's Line Drawing");
	myInit();
	glutDisplayFunc(myDisplay);

	//Question2- Triangle Sample Coverage
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(100, 100);
	glutCreateWindow("Sample Triangle  coverage");
	glutDisplayFunc(displayTriangle);

	//Question3- Anti Aliasing using Super Sampling
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE);
	glEnable(GL_MULTISAMPLE);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(200, 200);
	glutCreateWindow("Anti Aliasing using Super Sampling for Triangle");
	glutDisplayFunc(displayTriangle);
    glutMainLoop();
}