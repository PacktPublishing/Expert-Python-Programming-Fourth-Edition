import OpenGL.GL as gl
from OpenGL.GL import shaders


class lazy_class_attribute(object):
    def __init__(self, function):
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj or cls)
        # note: storing in class object not its instance
        #       no matter if its a class-level or
        #       instance-level access
        setattr(cls, self.fget.__name__, value)
        return value


class ObjectUsingShaderProgram(object):
    # trivial pass-through vertex shader implementation
    VERTEX_CODE = """ 
        #version 330 core 
        layout(location = 0) in vec4 vertexPosition; 
        void main(){ 
            gl_Position =  vertexPosition; 
        } 
    """
    # trivial fragment shader that results in everything
    # drawn with white color
    FRAGMENT_CODE = """ 
        #version 330 core 
        out lowp vec4 out_color; 
        void main(){ 
            out_color = vec4(1, 1, 1, 1); 
        } 
    """

    @lazy_class_attribute
    def shader_program(self):
        print("compiling!")
        return shaders.compileProgram(
            shaders.compileShader(self.VERTEX_CODE, gl.GL_VERTEX_SHADER),
            shaders.compileShader(self.FRAGMENT_CODE, gl.GL_FRAGMENT_SHADER),
        )
