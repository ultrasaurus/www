int interval = 200; 
int when = 0;
int jumpheight = 60;
int xstart = 0;
int ystart = 200;
int spacing = 4;

int count = 50;
int distance = count * spacing;
float pheight[] = new float[count]; 
int pwhen[] = new int[count]; 

void setup() 
{ 
  int i;
  for (i=0; i < count; i++) {
    pheight[i] = 20; 
    pwhen[i] = 0;
  }
  
  size(200, 200); 
  colorMode(RGB, 255, 255, 255); 
  stroke(0);
  ellipseMode(CENTER_DIAMETER); 
  background(255);
  rect(xstart, ystart, interval, -jumpheight);
  fill(0, 0, 255);
  stroke(0, 0, 255);
  
  
} 
 
void loop() 
{   
  float xpos, ypos, t;
  int i, c, change_index;
  
  change_index = mouseX/spacing - xstart;
  if (change_index >= 0 && change_index < count) {
    jumpheight = ystart - mouseY;
    pheight[change_index] = jumpheight;
    pwhen[change_index] = 0;
  }
  background(255);

  xpos = xstart;
  
  for (i=0; i < count; i++) {
    c = int((float)i/(float)count * 255);
    stroke(255-c, 100, 255);
    t = (float)pwhen[i] / (float)interval * 2;  /* 0 to 2 */
    ypos = ystart - (pheight[i] * sinfunc(t));
    xpos += spacing;
    ellipse(xpos, ypos, 2, 2); 
    
    pwhen[i]++;
    if (pwhen[i] > interval) pwhen[i]=0;
  }
  
 } 

float sinfunc(float t) 
{
    float a, v;
    a = t * PI/2;
    v = sin(a);

    return v;
}
