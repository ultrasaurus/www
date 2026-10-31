int interval = 200; 
int when = 0;
int jumpheight = 60;
int xstart = 100;
int ystart = 80;
int spacing = 4;
int space_height = 160;

int count = 20;
int distance = count * spacing;
float pheight[] = new float[count]; 
int pwhen[] = new int[count]; 
int psize[] = new int[count];
float turn = (2*PI)/count;
int last_index = 0;

int reset_btn_x = 145;
int reset_btn_y = 165;
int reset_btn_width = 50;
int reset_btn_height = 20;
BFont myfont; 

void setup() 
{ 
  reset(); 
  size(200, 200); 
  colorMode(RGB, 255, 255, 255); 
  stroke(0);
  ellipseMode(CENTER_DIAMETER); 
  background(200);
  //rect(xstart, ystart, interval, -jumpheight);

  

  myfont = loadFont("Futura-Medium.vlw.gz"); 

    
  drawResetButton(255);
  textFont(myfont, 14); 
  text("click anywhere\nin the white space or\ndrag the mouse to create patterns", 5, 170); 
} 
 
void reset()
{
  int i;
  for (i=0; i < count; i++) {
    pheight[i] = 20; 
    pwhen[i] = 0;
    psize[i] = 2;
  }

}
 
 
void loop() 
{   
  float xpos, ypos, t, jump, a;
  int i, c, change_index;
  float dx, dy, d;
  String str;
  
  fill(255);
  rect(0,0, 200, space_height);
    
  if (mousePressed == true) {
  
    if (mouseY < space_height) {
      dx = mouseX-width/2;
      dy = mouseY-height/2;
      d = sqrt(dx*dx + dy*dy);
      a = atan2(dy, dx);
      if (a < 0) a= 2*PI+a;
      change_index = (int)(a/turn);
      if (change_index >= 0 && change_index < count) {
        pheight[change_index] = d;
        pwhen[change_index] = interval/2;
      }
    }
  }

  xpos = xstart;
  
  for (i=0; i < count; i++) {
    float r = i*turn;
    
    push();
    c = int((float)i/(float)count * 255);
    stroke(255-c, 100, 255);
    t = (float)pwhen[i] / (float)interval * 2;  /* 0 to 2 */
    jump = pheight[i] * sinfunc(t);
    translate(xstart, ystart);
    rotate(r);
    translate(jump,0);
    ellipse(0, 0, psize[i], psize[i]); 
    pwhen[i]++;
    if (pwhen[i] > interval) pwhen[i]=0;
    pop();
  }
  
 } 

float sinfunc(float t) 
{
    float a, v;
    a = t * PI/2;
    v = sin(a);

    return v;
}

boolean reset_button_down = false;
void mousePressed()
{
      if (mouseY > space_height) {
          if (mouseX > reset_btn_x && mouseX < (reset_btn_x + reset_btn_width)
            && mouseY > reset_btn_y && mouseY < (reset_btn_y + reset_btn_height))
            {
                  drawResetButton(190);
                  reset_button_down = true;
            }
      }

}

void mouseReleased()
{
  if (reset_button_down) {
    reset_button_down = false;
    reset();
    drawResetButton(255);
  }

}

void drawResetButton(int fillcolor)
{
  fill(fillcolor);   
  stroke(0, 0, 255);
  rect(reset_btn_x, reset_btn_y, reset_btn_width, reset_btn_height);
  
  textFont(myfont, 24); 
  fill(0, 0, 255);
  text("reset", reset_btn_x+4, reset_btn_y+16);

}
