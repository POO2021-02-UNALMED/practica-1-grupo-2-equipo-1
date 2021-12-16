package gestorAplicacion.personas;
import java.io.Serializable;

public abstract class Empleado implements Serializable {
	
	private static final long serialVersionUID = 1L;
	protected int cedula;
	protected String nombre;
	protected float sueldo;
	
	public Empleado(int cedula, String nombre, float sueldo) {
		this.cedula = cedula;
		this.nombre = nombre;
		this.sueldo = sueldo;
	}
	
	public abstract String toString();
}
