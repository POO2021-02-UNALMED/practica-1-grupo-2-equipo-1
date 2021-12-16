package gestorAplicacion.personas;

public class Administrador extends Empleado{
	
	private static final long serialVersionUID = 1L;
	private String usuario;
	private String contrasena;
	
	public Administrador(int cedula, String nombre, float sueldo, String usuario, String contrasena) {
		super(cedula, nombre, sueldo);
		this.cedula = cedula;
		this.nombre = nombre;
		this.sueldo = sueldo;
		this.usuario = usuario;
		this.contrasena = contrasena;
	}
	
	public String toString() {
		return "El administrador " + this.nombre + " identificado con el número de cedula " + this.cedula + " tiene como funciones: supervisar el local, dirigir a los baristas y hacer uso correcto del sistema al que se le dio acceso";

	}

	public String getUsuario() {
		return usuario;
	}

	public String getContrasena() {
		return contrasena;
	}

	public void setUsuario(String usuario) {
		this.usuario = usuario;
	}

	public void setContrasena(String contrasena) {
		this.contrasena = contrasena;
	}
	
	
	
	

}
