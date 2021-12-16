package gestorAplicacion.noPersonas;
import java.util.ArrayList;

import gestorAplicacion.personas.*;
import uiMain.ActivarPromocion;


public class OrdenVirtual implements Orden{

	private static ArrayList<OrdenVirtual> ordenesVirtuales = new ArrayList<OrdenVirtual>();
	private static int nroOrdenes = 2000;
	private ArrayList<Bebida> bebidas = new ArrayList<Bebida> ();
	private Cliente cliente;
	private Barista barista;
	private Domiciliario domiciliario;
	private int nroOrden;
	private float costo;
	private static int ordenesCreadas;
	
	public OrdenVirtual(ArrayList<Bebida> bebidas, Cliente cliente, Barista barista, Domiciliario domiciliario) {
		this();
		this.nroOrden = nroOrdenes;
		nroOrdenes ++;
		this.bebidas = bebidas;
		this.cliente = cliente;
		this.barista = barista;
		this.domiciliario = domiciliario;
		float acumulado = 0;
		for (Bebida x: bebidas) acumulado += x.getPrecio();
		this.costo = acumulado;
		ordenesVirtuales.add(this);
	}
	
	public static int getOrdenesCreadas() {
		return ordenesCreadas;
	}

	public static void setOrdenesCreadas(int ordenesCreadas) {
		OrdenVirtual.ordenesCreadas = ordenesCreadas;
	}

	public OrdenVirtual() {
		ordenesCreadas ++;
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
	
public void reportarIncidente() {
		
		this.domiciliario.setIncidentes(true);
	}

	public String toString() {
		return this.barista.getNombre() + " le vendió a " + this.cliente.getNombre()+" la orden número " + this.nroOrden + " por un valor de " + this.costo;
	}
	
	public static ArrayList<OrdenVirtual> getOrdenesVirtuales() {
		return ordenesVirtuales;
	}

	public static void setOrdenesVirtuales(ArrayList<OrdenVirtual> ordenesVirtuales) {
		OrdenVirtual.ordenesVirtuales = ordenesVirtuales;
	}

	public static int getNroOrdenes() {
		return nroOrdenes;
	}

	public ArrayList<Bebida> getBebidas() {
		return bebidas;
	}

	public Cliente getCliente() {
		return cliente;
	}

	public Barista getBarista() {
		return barista;
	}

	public Domiciliario getDomiciliario() {
		return domiciliario;
	}

	public int getNroOrden() {
		return nroOrden;
	}

	public float getCosto() {
		return costo;
	}

	

	public static void setNroOrdenes(int nroOrdenes) {
		OrdenVirtual.nroOrdenes = nroOrdenes;
	}

	public void setBebidas(ArrayList<Bebida> bebidas) {
		this.bebidas = bebidas;
	}

	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}

	public void setBarista(Barista barista) {
		this.barista = barista;
	}

	public void setDomiciliario(Domiciliario domiciliario) {
		this.domiciliario = domiciliario;
	}

	public void setNroOrden(int nroOrden) {
		this.nroOrden = nroOrden;
	}

	public void setCosto(float costo) {
		this.costo = costo;
	}
	
}
