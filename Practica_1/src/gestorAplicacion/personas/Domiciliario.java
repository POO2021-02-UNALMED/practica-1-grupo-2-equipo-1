package gestorAplicacion.personas;

import java.util.ArrayList;
import java.io.Serializable;

public class Domiciliario implements Serializable {

	private static final long serialVersionUID = 1L;
	private static ArrayList<Domiciliario> domiciliarios = new ArrayList<Domiciliario>();
	private String nombre;
	private int codigo;
	private boolean incidentes;


	public Domiciliario(String nombre) {
		int id = (int)(Math.random()*9000)+1000;
		this.codigo = id;
		this.nombre = nombre;
		this.incidentes = false;
		domiciliarios.add(this);
		}

	public String getNombre() {
		return nombre;
	}

	public int getCodigo() {
		return codigo;
	}

	public boolean isIncidentes() {
		return incidentes;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public void setCodigo(int codigo) {
		this.codigo = codigo;
	}

	public void setIncidentes(boolean incidentes) {
		this.incidentes = incidentes;
	}
	
	public static ArrayList<Domiciliario> getDomiciliarios() {
		return domiciliarios;
	}

	public static void setDomiciliarios(ArrayList<Domiciliario> domiciliarios) {
		Domiciliario.domiciliarios = domiciliarios;
	}

	public String toString() {
		String incidentes;
		if (this.incidentes) {
			incidentes = "este domiciliario ha sido reportado previamente";
		}else {
			incidentes = "este domiciliario no ha sido reportado previamente";
		}
		return "\nLa orden fue asignada a " + this.nombre +"\n" + incidentes;
	}
	
}
