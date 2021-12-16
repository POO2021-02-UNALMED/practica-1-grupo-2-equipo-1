package gestorAplicacion.noPersonas;

public class Jugo extends Bebida{
	
	private static int inventarioJugo;
	private static int codigoJugo = 2000;
	private static final float PRECIOJUGO = 4000;
	
	public Jugo() {
		super(codigoJugo, PRECIOJUGO);
		this.codigo = codigoJugo;
		this.precio = PRECIOJUGO;
		inventarioJugo ++;
	}
	
	public String toString() {
		String activo = "\nJugo";
		String formatoFactura = String.format("%-25s",activo).replace(' ', '.');
		formatoFactura += this.precio;
		return formatoFactura;
	}
	
	


	public static int getInventarioJugo() {
		return inventarioJugo;
	}


	public static void setInventarioJugo(int inventarioJugo) {
		Jugo.inventarioJugo = inventarioJugo;
	}
	
	public static void prepararJugos(int i) {
		while(i>0) {
			new Jugo();
			i--;
		}
	}
}
	
