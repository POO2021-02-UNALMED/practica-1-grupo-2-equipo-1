package gestorAplicacion.personas;
import java.util.ArrayList;
import gestorAplicacion.noPersonas.*;

public class Barista extends Empleado{
	
	private static final long serialVersionUID = 1L;
	private static ArrayList<Barista> baristas = new ArrayList<Barista>();
	private ArrayList<Orden> ventas = new ArrayList<Orden> ();
	private float ventasAcumuladas;
	private float comisionVentas;
	private int comisionAcumulada;
	private static final float SUELDO = 908526;
	
	public Barista(int cedula, String nombre) {
		super(cedula, nombre, SUELDO);
		this.cedula = cedula;
		this.nombre = nombre;
		baristas.add(this);
	}
	
	public String toString() {
		return "El barista " + this.nombre + " identificado con el número de cedula " + this.cedula + " tiene como funciones: atender al cliente, vigilar el local y recibir ordenes por parte de su administrador";
		
	}
	
	
	
	public static ArrayList<Barista> getBaristas() {
		return baristas;
	}

	public static float getSueldo() {
		return SUELDO;
	}

	public static void setBaristas(ArrayList<Barista> baristas) {
		Barista.baristas = baristas;
	}

	public ArrayList<Orden> getOrdenes() {
		return ventas;
	}

	public float getComisionVentas() {
		return comisionVentas;
	}

	public void setOrdenes(ArrayList<Orden> ordenes) {
		this.ventas = ordenes;
	}
	
	public String getNombre() {
		return this.nombre;
	}

	public void setComisionVentas(float comisionVentas) {
		this.comisionVentas = comisionVentas;
	}
	
	public ArrayList<Orden> getVentas() {
		return ventas;
	}

	public float getVentasAcumuladas() {
		return ventasAcumuladas;
	}

	public int getComisionAcumulada() {
		return comisionAcumulada;
	}

	public void setVentas(ArrayList<Orden> ventas) {
		this.ventas = ventas;
	}

	public void setVentasAcumuladas(float ventasAcumuladas) {
		this.ventasAcumuladas = ventasAcumuladas;
	}

	public void setComisionAcumulada(int comisionAcumulada) {
		this.comisionAcumulada = comisionAcumulada;
	}

	public String prepararVenta(ArrayList<Bebida> bebidas, Cliente cliente){
		OrdenPresencial orden = new OrdenPresencial(bebidas, cliente, this);
		String retorno = "\nOrden "+orden.getNumeroOrden()+"\n\npreparada por\n" + this.nombre + "\n\npara\n" + cliente.getNombre()+"\n";
		for (Bebida x: bebidas) {
			retorno += x.toString();
		}
		String valorFactura = String.format("%-23s","Valor_total" ).replace(' ', '.');
		retorno += "\n" + valorFactura+ orden.getCosto();
		this.ventas.add(orden);
		this.ventasAcumuladas += orden.getCosto();
		this.comisionVentas += (orden.getCosto() * this.comisionAcumulada)/100;
		if (this.ventasAcumuladas >= 20000) {
			if (this.ventasAcumuladas >= 50000) {
				this.comisionAcumulada = 5;
			}
			else {
				this.comisionAcumulada = 2;
			}
		}
		
		return retorno;
	}
	
	public String prepararVenta(ArrayList<Bebida> bebidas, Cliente cliente, Promocion promocion){
		OrdenPresencial orden = new OrdenPresencial(bebidas, cliente, this);
		orden.aplicarPromocion(promocion);
		String retorno = "\nOrden "+orden.getNumeroOrden()+"\n\npreparada por\n"+ this.nombre + "\n\npara\n" + cliente.getNombre()+"\n";
		for (Bebida x: bebidas) {
			retorno += x.toString();
		}
		String valorFactura = String.format("%-23s","Valor_con_promo" ).replace(' ', '.');
		retorno += "\n" + valorFactura+ orden.getCosto();
		this.ventas.add(orden);
		this.ventasAcumuladas += orden.getCosto();
		this.comisionVentas += (orden.getCosto() * this.comisionAcumulada)/100;
		if (this.ventasAcumuladas >= 20000) {
			if (this.ventasAcumuladas >= 50000) {
				this.comisionAcumulada = 5;
			}
			else {
				this.comisionAcumulada = 2;
			}
		}
		
		return retorno;
	}
	
	
	public String prepararVenta(ArrayList<Bebida> bebidas, Cliente cliente, Domiciliario domiciliario){
		OrdenVirtual orden = new OrdenVirtual(bebidas, cliente, this, domiciliario);
		String retorno = "\nOrden "+orden.getNroOrden()+"\n\npreparada por\n"+ this.nombre +"\n\nse le entrega a\n"+ domiciliario.getNombre() + "\n\npara ser entregada a \n" + cliente.getNombre()+"\n";
		for (Bebida x: bebidas) {
			retorno += x.toString();
		}
		String valorFactura = String.format("%-23s","Valor_total" ).replace(' ', '.');
		retorno += "\n" + valorFactura+ orden.getCosto();
		this.ventas.add(orden);
		this.ventasAcumuladas += orden.getCosto();
		this.comisionVentas += (orden.getCosto() * this.comisionAcumulada)/100;
		if (this.ventasAcumuladas >= 20000) {
			if (this.ventasAcumuladas >= 50000) {
				this.comisionAcumulada = 5;
			}
			else {
				this.comisionAcumulada = 2;
			}
		}
		
		return retorno;
		
	}
	
	public String prepararVenta(ArrayList<Bebida> bebidas, Cliente cliente, Domiciliario domiciliario, Promocion promocion){
		OrdenVirtual orden = new OrdenVirtual(bebidas, cliente, this, domiciliario);
		orden.aplicarPromocion(promocion);
		String retorno = "\nOrden "+orden.getNroOrden()+"\n\npreparada por\n"+ this.nombre +"\n\nse le entrega a\n"+ domiciliario.getNombre() + "\n\npara ser entregada a \n" + cliente.getNombre()+"\n";
		for (Bebida x: bebidas) {
			retorno += x.toString();
		}
		String valorFactura = String.format("%-23s","Valor_con_promo" ).replace(' ', '.');
		retorno += "\n" + valorFactura+ orden.getCosto();
		this.ventas.add(orden);
		this.ventasAcumuladas += orden.getCosto();
		this.comisionVentas += (orden.getCosto() * this.comisionAcumulada)/100;
		if (this.ventasAcumuladas >= 20000) {
			if (this.ventasAcumuladas >= 50000) {
				this.comisionAcumulada = 5;
			}
			else {
				this.comisionAcumulada = 2;
			}
		}
		
		return retorno;
		
	}	
}
