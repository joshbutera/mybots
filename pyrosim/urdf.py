class URDF:

    def __init__(self):

        self.depth = 0

    def Save_Start_Tag(self,f):

        f.write('<robot name = "robot">\n' +
        '    <material name="blue">\n'
        '        <color rgba="0 0 1.0 1.0"/>\n'
        '    </material>\n' +
        '    <material name="green">\n'
        '        <color rgba="0 1.0 0 1.0"/>\n'
        '    </material>\n')

    def Save_End_Tag(self,f):

        f.write("</robot>")
