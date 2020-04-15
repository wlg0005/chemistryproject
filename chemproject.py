from vpython import *

scene.width = 600
scene.height=1000
scene.background = color.white
scene.range = 1.3
scene.title = '<h1>CH 121-02 Exam 4 Project - Will Green</h1>'
scene.align = 'left'
scene.caption = ''

# linear shape to start
# molecule object
molecule1 = sphere(pos=vector(0,0,0), radius=0.15, color=color.blue) # center
molecule2 = sphere(pos=vector(0.5,0,0), radius=0.125,color=color.blue) # right
molecule3 = sphere(pos=vector(-0.5,0,0), radius=0.125,color=color.blue) # left

#bond objects
bond1 = cylinder(pos=vector(0,0,0),axis=vector(0.5,0,0), radius=0.0625,color=color.white) # right
bond2 = cylinder(pos=vector(0,0,0),axis=vector(-0.5,0,0), radius=0.0625,color=color.white) # left

angle = label(text=str(degrees(diff_angle(bond1.axis,bond2.axis)))+'°',height=15,pos=vector(0,.25,0),color=color.black)

info = label(text='Molecular Geometries:\n2 atoms bound = linear\n1 atom bound, 1 lone pair = linear',height=20,pos=vector(0,1.5,0),color=color.black)


def M(m):

    # ------------------ LINEAR ------------------
    if m.selected == 'linear':
        # clear previous objects
        for obj in scene.objects:
            obj.visible = False
            
        # ------------------ molecule objects ------------------
        molecule1 = sphere(pos=vector(0,0,0), radius=0.15, color=color.blue) # center
        molecule2 = sphere(pos=vector(0.5,0,0), radius=0.125,color=color.blue) # right
        molecule3 = sphere(pos=vector(-0.5,0,0), radius=0.125,color=color.blue) # left
        
        # ------------------ bond objects ------------------
        bond1 = cylinder(pos=vector(0,0,0),axis=vector(0.5,0,0), radius=0.0625,color=color.white) # right
        bond2 = cylinder(pos=vector(0,0,0),axis=vector(-0.5,0,0), radius=0.0625,color=color.white) # left
        
        #angle
        angle = label(text=str(degrees(diff_angle(bond1.axis,bond2.axis)))+'°',height=15,pos=vector(0,.25,0),color=color.black)

        #info
        info = label(text='Molecular Geometries:\n2 atoms bound = linear\n1 atom bound, 1 lone pair = linear',height=20,pos=vector(0,1.5,0),color=color.black)

    # ------------------ TRIGONAL PLANAR ------------------   
    elif m.selected == 'trigonal planar':
        # clear previous objects
        for obj in scene.objects:
            obj.visible = False

        # ------------------ molecule objects ------------------
        molecule1 = sphere(pos=vector(0,0,0), radius=0.15, color=color.blue) # center

        molecule2 = sphere(pos=vector(0.5,0,0), radius=0.125,color=color.blue) # right
        molecule2.rotate(angle=radians(-30),axis=vector(0,0,1),origin=vector(0,0,0)) # rotation

        molecule3 = sphere(pos=vector(-0.5,0,0), radius=0.125,color=color.blue) # left
        molecule3.rotate(angle=radians(30),axis=vector(0,0,1),origin=vector(0,0,0)) # rotation

        molecule4 = sphere(pos=vector(0,0.5,0), radius=0.125,color=color.blue) # top

        # ------------------ bond objects ------------------
        bond1 = cylinder(pos=vector(0,0,0),axis=vector(0.5,0,0), radius=0.0625, color=color.white) # right
        bond1.rotate(angle=radians(-30), axis=vector(0,0,1)) # rotation
        
        bond2 = cylinder(pos=vector(0,0,0),axis=vector(-0.5,0,0), radius=0.0625,color=color.white) # left
        bond2.rotate(angle=radians(30), axis=vector(0,0,1)) # rotation
        
        bond3 = cylinder(pos=vector(0,0,0), axis=vector(0,0.5,0), radius=0.0625, color=color.white) # top

        # angles
        angle1 = label(text=str(round(degrees(diff_angle(bond1.axis, bond2.axis)),4))+'°',height=15,pos=vector(0.25,.25,0),color=color.black)
        angle2 = label(text=str(round(degrees(diff_angle(bond1.axis, bond3.axis)),4))+'°',height=15,pos=vector(0,-.25,0),color=color.black)
        angle3 = label(text=str(round(degrees(diff_angle(bond2.axis, bond3.axis)),4))+'°',height=15,pos=vector(-0.25,.25,0),color=color.black)

        #info
        info = label(text='Molecular Geometries:\n3 atoms bound = trigonal planar\n2 atoms bound, 1 lone pair = bent\n1 atom bound, 2 lone pairs = linear',height=20,pos=vector(0,1.5,0),color=color.black)
        
    # ------------------ TETRAHEDRAL ------------------ 
    elif m.selected == 'tetrahedral':
        # clear previous objects
        for obj in scene.objects:
            obj.visible = False
            
        # ------------------ molecule objects ------------------
        molecule1 = sphere(pos=vector(0,0,0), radius=0.15, color=color.blue) # center
        
        molecule2 = sphere(pos=vector(0.5,0,0), radius=0.125, color=color.blue) # right
        molecule2.rotate(angle=radians(-19.5), axis=vector(0,0,1),origin=vector(0,0,0)) # rotation
        molecule2.rotate(angle=radians(-29.25), axis=vector(0,1,0),origin=vector(0,0,0)) # rotation

        molecule3 = sphere(pos=vector(-0.5,0,0), radius=0.125, color=color.blue) # left
        molecule3.rotate(angle=radians(19.5), axis=vector(0,0,1),origin=vector(0,0,0)) # rotation
        molecule3.rotate(angle=radians(29.25), axis=vector(0,1,0),origin=vector(0,0,0)) # rotation

        molecule4 = sphere(pos=vector(0,0,-0.5), radius=0.125, color=color.blue) # back
        molecule4.rotate(angle=radians(-19.5),axis=vector(1,0,0),origin=vector(0,0,0)) # rotation

        molecule5 = sphere(pos=vector(0,0.5,0), radius=0.125, color=color.blue) # top

        # ------------------ bond objects ------------------
        bond1 = cylinder(pos=vector(0,0,0),axis=vector(0.5,0,0), radius=0.0625, color=color.white) # right
        bond1.rotate(angle=radians(-19.5), axis=vector(0,0,1)) # rotation
        bond1.rotate(angle=radians(-29.5), axis=vector(0,1,0)) # rotation
        
        bond2 = cylinder(pos=vector(0,0,0),axis=vector(-0.5,0,0), radius=0.0625, color=color.white) # left
        bond2.rotate(angle=radians(19.5), axis=vector(0,0,1)) # rotation
        bond2.rotate(angle=radians(29.5), axis=vector(0,1,0)) # rotation

        bond3 = cylinder(pos=vector(0,0,0), axis=vector(0,0,-0.5), radius=0.0625, color=color.white) # back
        bond3.rotate(angle=radians(-19.5),axis=vector(1,0,0)) # rotation
        
        bond4 = cylinder(pos=vector(0,0,0), axis=vector(0,0.5,0), radius=0.0625, color=color.white) # top

        # angle objects
        angle1 = label(text=str(round(degrees(diff_angle(bond1.axis, bond4.axis)),4))+'°',height=15,pos=vector(0.25,.25,0.15),color=color.black) # right
        angle2 = label(text=str(round(degrees(diff_angle(bond2.axis, bond4.axis)),4))+'°',height=15,pos=vector(-0.25,.25,0.15),color=color.black) # left
        angle3 = label(text=str(round(degrees(diff_angle(bond4.axis, bond1.axis)),4))+'°',height=15,pos=vector(0,-.25,0.25),color=color.black) # front

        #info
        info = label(text='Molecular Geometries:\n4 atoms bound = tetrahedral\n3 atoms, 1 lone pair = trigonal pyramidal\n2 atoms, 2 lone pairs = bent\n1 atom, 3 lone pairs = linear',height=20,pos=vector(0,1.5,0),color=color.black)
    # ------------------ TRIGONAL BIPYRAMIDAL ------------------
    elif m.selected == 'trigonal bipyramidal':
        # clear previous objects
        for obj in scene.objects:
            obj.visible = False
            
        # ------------------ molecule objects ------------------
        molecule1 = sphere(pos=vector(0,0,0), radius=0.15, color=color.blue) # center
        molecule2 = sphere(pos=vector(0.5,0,0),radius=0.125, color=color.blue) # right
        molecule3 = sphere(pos=vector(0,0.5,0), radius=0.125, color=color.blue) # top
        molecule4 = sphere(pos=vector(-0.5,0,0), radius=0.125, color=color.blue) # left
        
        molecule5 = sphere(pos=vector(0,0,0.5), radius=0.125, color=color.blue) # front
        molecule5.rotate(angle=radians(30),axis=vector(1,0,0),origin=vector(0,0,0)) # rotation
        
        molecule6 = sphere(pos=vector(0,0,-0.5), radius=0.125, color=color.blue) # back
        molecule6.rotate(angle=radians(-30), axis=vector(1,0,0),origin=vector(0,0,0)) # rotation

        #------------------ bond objects ------------------
        bond1 = cylinder(pos=vector(0,0,0), axis=vector(0.5,0,0), radius=0.0625, color=color.white) # right
        bond2 = cylinder(pos=vector(0,0,0), axis=vector(-0.5,0,0), radius=0.0625, color=color.white) # left
        bond3 = cylinder(pos=vector(0,0,0), axis=vector(0,0.5,0), radius=0.0625, color=color.white) # top
        
        bond4 = cylinder(pos=vector(0,0,0), axis=vector(0,0,0.5), radius=0.0625, color=color.white) # front
        bond4.rotate(angle=radians(30),axis=vector(1,0,0),origin=vector(0,0,0)) # rotation
        
        bond5 = cylinder(pos=vector(0,0,0), axis=vector(0,0,-0.5), radius=0.0625, color=color.white) # back
        bond5.rotate(angle=radians(-30), axis=vector(1,0,0),origin=vector(0,0,0)) # rotation

        # angles
        angle1 = label(text=str(degrees(diff_angle(bond1.axis,bond3.axis)))+'°',height=15,pos=vector(0.25,0.25,0),color=color.black) # right
        angle2 = label(text=str(round(degrees(diff_angle(bond2.axis, bond3.axis)),4))+'°',height=15,pos=vector(-0.25,0.25,0),color=color.black) # left
        angle3 = label(text=str(round(degrees(diff_angle(bond3.axis, bond4.axis)),4))+'°',height=15,pos=vector(0,.25,0.25),color=color.black) # front
        angle4 = label(text=str(round(degrees(diff_angle(bond3.axis,bond5.axis)),4))+'°',height=15,pos=vector(0,0.25,-0.25),color=color.black) # back
        angle5 = label(text=str(round(degrees(diff_angle(bond4.axis,bond5.axis)),4))+'°',height=15,pos=vector(0,-.25,0),color=color.black) # bottom

        # info
        info = label(text='Molecular Geometries:\n5 atoms bound = trigonal bipyramidal\n4 atom bound, 1 lone pair = seesaw\n3 atom bound, 2 lone pair = T-shaped\n 2 atom bound, 3 lone pair = linear\n1 atom bound, 4 lone pair = linear',height=20,pos=vector(0,1.5,0),color=color.black)

        
    # ------------------ OCTAHEDRAL ------------------
    elif m.selected == 'octahedral':
        # clear previous objects
        for obj in scene.objects:
            obj.visible = False
            
        # ------------------ molecule objects ------------------ 
        molecule1 = sphere(pos=vector(0,0,0), radius=0.15, color=color.blue) # center
        molecule2 = sphere(pos=vector(0.5,0,0),radius=0.125, color=color.blue) # right
        molecule3 = sphere(pos=vector(-0.5,0,0),radius=0.125, color=color.blue) # left
        molecule4 = sphere(pos=vector(0,0.5,0),radius=0.125, color=color.blue) # top
        molecule5 = sphere(pos=vector(0,-0.5,0),radius=0.125, color=color.blue) # bottom
        molecule6 = sphere(pos=vector(0,0,0.5),radius=0.125, color=color.blue) # front
        molecule7 = sphere(pos=vector(0,0,-0.5),radius=0.125, color=color.blue) # back
        
        # ------------------ bond objects ------------------
        bond1 = cylinder(pos=vector(0,0,0), axis=vector(0.5,0,0), radius=0.0625, color=color.white) # right
        bond2 = cylinder(pos=vector(0,0,0), axis=vector(-0.5,0,0), radius=0.0625, color=color.white) # left
        bond3 = cylinder(pos=vector(0,0,0), axis=vector(0,0.5,0), radius=0.0625, color=color.white) # top
        bond4 = cylinder(pos=vector(0,0,0), axis=vector(0,-0.5,0), radius=0.0625, color=color.white) # bottom
        bond5 = cylinder(pos=vector(0,0,0), axis=vector(0,0,0.5), radius=0.0625, color=color.white) # front
        bond6 = cylinder(pos=vector(0,0,0), axis=vector(0,0,-0.5), radius=0.0625, color=color.white) # back

        #angles
        angle1 = label(text=str(degrees(diff_angle(bond1.axis,bond3.axis)))+'°',height=15,pos=vector(0.25,0.25,0),color=color.black) # right
        angle2 = label(text=str(degrees(diff_angle(bond2.axis,bond3.axis)))+'°',height=15,pos=vector(-0.25,0.25,0),color=color.black) # left
        angle3 = label(text=str(degrees(diff_angle(bond3.axis,bond5.axis)))+'°',height=15,pos=vector(0,0.25,0.25),color=color.black) # front
        angle4 = label(text=str(degrees(diff_angle(bond3.axis,bond6.axis)))+'°',height=15,pos=vector(0,0.25,-0.25),color=color.black) # back

        #info
        info = label(text='Molecular Geometries:\n6 atoms bound = octahedral\n5 atoms bound, 1 lone pair = square pyramidal\n4 atoms bound, 2 lone pairs = square planar\n3 atoms bound, 3 lone pairs = T-shaped\n2 atoms bound, 4 lone pairs = linear\n1 atom bound, 5 lone pairs = linear',height=20,pos=vector(0,1.5,0),color=color.black)

    # ------------------ METHANE ------------------
    elif m.selected == 'Methane (CH4)':
        # clear previous objects
        for obj in scene.objects:
            obj.visible = False

        # ------------------ molecule objects ------------------
        molecule1 = sphere(pos=vector(0,0,0), radius=0.15, color=color.blue) # center
        
        molecule2 = sphere(pos=vector(0.5,0,0), radius=0.125, color=color.blue) # right
        molecule2.rotate(angle=radians(-19.5), axis=vector(0,0,1),origin=vector(0,0,0)) # rotation
        molecule2.rotate(angle=radians(-29.25), axis=vector(0,1,0),origin=vector(0,0,0)) # rotation

        molecule3 = sphere(pos=vector(-0.5,0,0), radius=0.125, color=color.blue) # left
        molecule3.rotate(angle=radians(19.5), axis=vector(0,0,1),origin=vector(0,0,0)) # rotation
        molecule3.rotate(angle=radians(29.25), axis=vector(0,1,0),origin=vector(0,0,0)) # rotation

        molecule4 = sphere(pos=vector(0,0,-0.5), radius=0.125, color=color.blue) # back
        molecule4.rotate(angle=radians(-19.5),axis=vector(1,0,0),origin=vector(0,0,0)) # rotation

        molecule5 = sphere(pos=vector(0,0.5,0), radius=0.125, color=color.blue) # top

        # ------------------ bond objects ------------------
        bond1 = cylinder(pos=vector(0,0,0),axis=vector(0.5,0,0), radius=0.0625, color=color.white) # right
        bond1.rotate(angle=radians(-19.5), axis=vector(0,0,1)) # rotation
        bond1.rotate(angle=radians(-29.5), axis=vector(0,1,0)) # rotation
        
        bond2 = cylinder(pos=vector(0,0,0),axis=vector(-0.5,0,0), radius=0.0625, color=color.white) # left
        bond2.rotate(angle=radians(19.5), axis=vector(0,0,1)) # rotation
        bond2.rotate(angle=radians(29.5), axis=vector(0,1,0)) # rotation

        bond3 = cylinder(pos=vector(0,0,0), axis=vector(0,0,-0.5), radius=0.0625, color=color.white) # back
        bond3.rotate(angle=radians(-19.5),axis=vector(1,0,0)) # rotation
        
        bond4 = cylinder(pos=vector(0,0,0), axis=vector(0,0.5,0), radius=0.0625, color=color.white) # top

        # angle objects
        angle1 = label(text=str(round(degrees(diff_angle(bond1.axis, bond4.axis)),4))+'°',height=15,pos=vector(0.25,.25,0.15),color=color.black) # right
        angle2 = label(text=str(round(degrees(diff_angle(bond2.axis, bond4.axis)),4))+'°',height=15,pos=vector(-0.25,.25,0.15),color=color.black) # left
        angle3 = label(text=str(round(degrees(diff_angle(bond4.axis, bond1.axis)),4))+'°',height=15,pos=vector(0,-.25,0.25),color=color.black) # front

        info = label(text='Methane (CH4):\nShape: tetrahedral\nBond angles: 109.5°\nHybridization: sp3\nPolarity: Non-polar',height=20,pos=vector(0,1.5,0),color=color.black)
            
    
# menu
menu( choices=['linear', 'trigonal planar', 'tetrahedral', 'trigonal bipyramidal', 'octahedral','Methane (CH4)'], bind=M, pos=scene.caption_anchor)

# caption
scene.append_to_caption("""
<div width="50%" height="50%">
To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
On a two-button mouse, middle is left + right.
To pan Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate.
<h2>Overview:</h2>
<li>The VSEPR (Valence Shell Electron Pair Repulsion) demonstrates how two or more atoms
bound to a central atom will try and get as far away from each other as possible
while still being attached to the central atom.</li>
<h2>Molecular Geometry</h2>
<li> The geometry of a molecule refers to the shape that its bonds create.
There are many different shapes such as: linear, trigonal planar, tetrahedral, and many more!</li>
<h2>Bond Angles</h2>
<li>Bond angles refer to the angles that are created between bonds based off how the molecules
arrange themselves in order to get the furthest distance away from one another</li>
<li>There must be at least 3 molecules for a bond angle to occur.</li>
<li>Example: Checkout Methane (CH4) in the dropdown!</li>
<h2>Orbital Hybridization</h2>
<li>Orbital hybridization occurs when the orbitals for the electrons (s,p,d,f) are more stable
when combined rather than a full S orbital and an empty p, which results in a hybrid orbital of sp.
<li>Methane has a hybridization of sp3</li>
<h2>Molecular Polarity</h2>
<li>Molecular polarity is the charge imbalance and bond polarity of an atom.</li>
<li>Molecules that are polar carry a charge (+/-) and if it is nonpolar there is no charge.</li>
<li>Methane has polar bonds, but it is a nonpolar molecule because its regular tetrahedron shape leads to a symmetrical distribution of the molecules partial charges.</li>

<style>
select {width:150px;}
select {height:50px;}
</style


""")
