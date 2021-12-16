package gestorAplicacion.noPersonas;
import java.util.ArrayList;
import gestorAplicacion.personas.*;
import uiMain.ActivarPromocion;


public class OrdenPresencial implements Orden {
	
	
	private static int numeroOrdenes = 1000;
	private ArrayList<Bebida> bebidas = new ArrayList<Bebida> ();
	private Cliente cliente;
	private Barista barista;
	private int numeroOrden;
	private float costo;
	private static int ordenesCreadas;
	
	
	public OrdenPresencial(ArrayList<Bebida> bebidas, Cliente cliente, Barista barista) {
		this();
		this.numeroOrden = numeroOrdenes;
		numeroOrdenes ++;
		this.bebidas = bebidas;
		this.cliente = cliente;
		this.barista = barista;
		float acumulado = 0;
		for (Bebida x: bebidas) acumulado += x.getPrecio();
		this.costo = acumulado;
	}
	
	public OrdenPresencial() {
		ordenesCreadas++;
	}
	
	public ArrayList<Bebida> getBebidas() {
		return bebidas;
	}

	public static int getOrdenesCreadas() {
		return ordenesCreadas;
	}

	public void setBebidas(ArrayList<Bebida> bebidas) {
		this.bebidas = bebidas;
	}

	public static void setOrdenesCreadas(int ordenesCreadas) {
		OrdenPresencial.ordenesCreadas = ordenesCreadas;
	}

	public void aplicarPromocion(Promocion promocion) {
		if(promocion.equals(Promocion.CAFE2X1) && ActivarPromocion.isPromos()) {
			this.costo -= 5000;
		} else if(promocion.equals(Promocion.JUGO2X1) && ActivarPromocion.isPromos()) {
			this.costo -= 4000;
		} else if (promocion.equals(Promocion.CAFECONJUGOAL50) && ActivarPromocion.isPromos()){
			this.costo -= 4500;
		}
	}
	
	public String toString() {
		return this.barista.getNombre() + " le vendió a " + this.cliente.getNombre()+" la orden número " + this.numeroOrden + " por un valor de " + this.costo;
	}


	public static int getNumeroOrdenes() {
		return numeroOrdenes;
	}


	public ArrayList<Bebida> getProductos() {
		return bebidas;
	}


	public Cliente getCliente() {
		return cliente;
	}


	public Barista getBarista() {
		return barista;
	}


	public int getNumeroOrden() {
		return numeroOrden;
	}


	public float getCosto() {
		return costo;
	}


	public static void setNumeroOrdenes(int numeroOrdenes) {
		OrdenPresencial.numeroOrdenes = numeroOrdenes;
	}


	public void setProductos(ArrayList<Bebida> bebidas) {
		this.bebidas = bebidas;
	}


	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}


	public void setBarista(Barista barista) {
		this.barista = barista;
	}


	public void setNumeroOrden(int numeroOrden) {
		this.numeroOrden = numeroOrden;
	}


	public void setCosto(float costo) {
		this.costo = costo;
	}
	
}
