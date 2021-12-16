package gestorAplicacion.noPersonas;

public class Bebida {

	protected int codigo;
	protected float precio;
	
	public Bebida(int codigo, float precio) {
		this.codigo = codigo;
		this.precio = precio;
	}
	
	public String toString() {
		return "La bebida preparada tiene un precio de " + this.precio;
	}

	public int getCodigo() {
		return codigo;
	}

	public float getPrecio() {
		return precio;
	}

	public void setCodigo(int codigo) {
		this.codigo = codigo;
	}

	public void setPrecio(float precio) {
		this.precio = precio;
	}

	public void fueVendido() {
	}
	
	
}
