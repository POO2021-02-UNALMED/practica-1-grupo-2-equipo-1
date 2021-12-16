package gestorAplicacion.noPersonas;



public class Cafe extends Bebida{
	
	private static int inventarioCafe;
	private static int codigoCafe = 1000;
	private static final float PRECIOCAFE = 5000;


	public Cafe() {
		super(codigoCafe, PRECIOCAFE);
		this.codigo = codigoCafe;
		codigo++;
		this.precio = PRECIOCAFE;
		inventarioCafe ++;
		
	}
	
	public static int getInventarioCafe() {
		return inventarioCafe;
	}

	public static void setInventarioCafe(int inventarioCafe) {
		Cafe.inventarioCafe = inventarioCafe;
	}

	public String toString() {
		String activo = "\nCafe";
		String formatoFactura = String.format("%-25s",activo).replace(' ', '.');
		formatoFactura += this.precio;
		return formatoFactura;
	}
	
	public static void prepararCafes(int i) {
		while(i>0) {
			new Cafe();
			i--;
		}
	}
	
	
	
	
	
	
}
