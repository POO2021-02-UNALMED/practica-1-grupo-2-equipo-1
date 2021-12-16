package uiMain;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Random;
import gestorAplicacion.personas.*;
import gestorAplicacion.noPersonas.*;

public class registroVenta {
	
	
	
	public static void start() {
		
		Scanner sc1 = new Scanner(System.in);
		System.out.print("\nLa orden es: \n1. Presencial\n2. Virtual\n\nIngresa 1 o 2 dependiendo de la orden: ");
		int eleccionVenta = sc1.nextInt();
		switch(eleccionVenta) {
		case 1: esPresencial();
				break;
		case 2: esVirtual();
				break;
		}
	}
	
	private static void esPresencial() {
		Barista elegido;
		ArrayList<Bebida> pedido = new ArrayList<Bebida>();
		Scanner sc1 = new Scanner(System.in);
		Scanner sc2 = new Scanner(System.in);
		System.out.println("\nIndica qué barista será el encargado de la orden:\n");
		for (int i = 0; i<Barista.getBaristas().size(); i++) {
			String renglon = (i+1) + ". " + Barista.getBaristas().get(i).getNombre();
			System.out.println(renglon);
		}
		System.out.print("\nIngresa 1, 2 o 3 dependiendo del barista: ");
		int barista = sc1.nextInt();
		elegido = Barista.getBaristas().get(barista-1);
		System.out.print("\n¿Cuál es el nombre del cliente?\n");
		String clienteIngresado = sc2.nextLine();
		Cliente cliente = new Cliente(clienteIngresado);
		System.out.println("\n¿Cuántos cafés quiere llevar?(Ingrese 0 si no lleva café)\n");
		int nroCafes = sc2.nextInt();
		if (nroCafes <= Cafe.getInventarioCafe()) {
			
				
			
			System.out.println("\n¿Cuántos jugos quiere llevar?(Ingrese 0 si no lleva jugo)\n");
			int nroJugos = sc2.nextInt();
			if (nroJugos <= Jugo.getInventarioJugo()) {
				System.out.print("\nIngresa 0 para continuar: ");
				int continuar1 = sc2.nextInt();
				Promocion promocion;
				if (ActivarPromocion.isPromos()) {
					System.out.println("\n¿Qué promoción quieres activar en esta orden?\n\n1. CAFE2X1\n2. JUGO2X1\n3. CAFECONJUGOAL50\n4. Ninguna\n");
					int x = sc1.nextInt();
					if (x == 1) {
						if(nroCafes >= 2) {
							promocion = Promocion.CAFE2X1;
							while (nroCafes > 0) {
								pedido.add(new Cafe());
								Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
								nroCafes --;}
							while (nroJugos > 0) {
								pedido.add(new Jugo());
								Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
								nroJugos --;}
							
							System.out.println(elegido.prepararVenta(pedido, cliente,promocion));
							System.out.print("\nIngresa 0 para continuar: ");
							int continuar2 = sc2.nextInt();
						}else {
							System.out.println("El pedido no cumplía con los requisitos de la promoción");
						}
					}else if(x == 2) {
						if(nroJugos >= 2) {
							promocion = Promocion.JUGO2X1;
							while (nroCafes > 0) {
								pedido.add(new Cafe());
								Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
								nroCafes --;}
							while (nroJugos > 0) {
								pedido.add(new Jugo());
								Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
								nroJugos --;}
							
							System.out.println(elegido.prepararVenta(pedido, cliente,promocion));
							System.out.print("\nIngresa 0 para continuar: ");
							int continuar2 = sc2.nextInt();
						}else {
							System.out.println("El pedido no cumplía con los requisitos de la promoción");
						}
					} else if(x == 3) {
						if(nroCafes >= 1 && nroJugos >= 1) {
							promocion = Promocion.CAFECONJUGOAL50;
							while (nroCafes > 0) {
								pedido.add(new Cafe());
								Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
								nroCafes --;}
							while (nroJugos > 0) {
								pedido.add(new Jugo());
								Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
								nroJugos --;}
							
							System.out.println(elegido.prepararVenta(pedido, cliente,promocion));
							System.out.print("\nIngresa 0 para continuar: ");
							int continuar2 = sc2.nextInt();
						}else {
							System.out.println("El pedido no cumplía con los requisitos de la promoción");
						}
					}else {
				
				while (nroCafes > 0) {
					pedido.add(new Cafe());
					Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
					nroCafes --;}
				while (nroJugos > 0) {
					pedido.add(new Jugo());
					Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
					nroJugos --;}
				
				System.out.println(elegido.prepararVenta(pedido, cliente));
				System.out.print("\nIngresa 0 para continuar: ");
				int continuar2 = sc2.nextInt();
			}}else {
				
				while (nroCafes > 0) {
					pedido.add(new Cafe());
					Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
					nroCafes --;}
				while (nroJugos > 0) {
					pedido.add(new Jugo());
					Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
					nroJugos --;}
				
				System.out.println(elegido.prepararVenta(pedido, cliente));
				System.out.print("\nIngresa 0 para continuar: ");
				int continuar2 = sc2.nextInt();
			}
				}
			else {
				System.out.println("No hay suficientes jugos para completar la orden");
				
			}
			
		}else {
			System.out.println("No hay suficientes cafés para completar la orden");
			
		}
		
			}
	
	
	private static void esVirtual() {
		Barista elegido;
		ArrayList<Bebida> pedido = new ArrayList<Bebida>();
		Scanner sc1 = new Scanner(System.in);
		Scanner sc2 = new Scanner(System.in);
		System.out.println("\nIndica qué barista será el encargado de la orden:\n");
		for (int i = 0; i<Barista.getBaristas().size(); i++) {
			String renglon = (i+1) + ". " + Barista.getBaristas().get(i).getNombre();
			System.out.println(renglon);
		}
		System.out.print("\nIngresa 1, 2 o 3 dependiendo del barista: ");
		int barista = sc1.nextInt();
		elegido = Barista.getBaristas().get(barista-1);
		System.out.print("\n¿Cuál es el nombre del cliente?\n");
		String clienteIngresado = sc2.nextLine();
		Cliente cliente = new Cliente(clienteIngresado);
		System.out.println("\n¿Cuántos cafés quiere llevar?(Ingrese 0 si no lleva café)\n");
		int nroCafes = sc2.nextInt();
		if (nroCafes <= Cafe.getInventarioCafe()) {
			
				
			
			System.out.println("\n¿Cuántos jugos quiere llevar?(Ingrese 0 si no lleva jugo)\n");
			int nroJugos = sc2.nextInt();
			if (nroJugos <= Jugo.getInventarioJugo()) {
				System.out.print("\nIngresa 0 para continuar: ");
				int continuar1 = sc2.nextInt();
				Promocion promocion;
				if (ActivarPromocion.isPromos()) {
					System.out.println("\n¿Qué promoción quieres activar en esta orden?\n\n1. CAFE2X1\n2. JUGO2X1\n3. CAFECONJUGOAL50\n4. Ninguna\n");
					int x = sc1.nextInt();
					if (x == 1) {
						if(nroCafes >= 2) {
							promocion = Promocion.CAFE2X1;
							Random r = new Random();
							int randomNumber = r.nextInt(Domiciliario.getDomiciliarios().size());
							Domiciliario domiciliario = Domiciliario.getDomiciliarios().get(randomNumber);
							System.out.println(domiciliario.toString());
							if (domiciliario.isIncidentes()) {
							System.out.print("\nIngresa 0 para rechazar la orden o 1 para continuar, ignorando el reporte: ");
							int continuar2 = sc2.nextInt();
							if (continuar2 == 1) {
								while (nroCafes > 0) {
									pedido.add(new Cafe());
									Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
									nroCafes --;}
								while (nroJugos > 0) {
									pedido.add(new Jugo());
									Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
									nroJugos --;}
								System.out.println(elegido.prepararVenta(pedido, cliente, domiciliario, promocion));
								System.out.print("\nIngresa 0 para continuar: ");
								int continuar3 = sc2.nextInt();
							}
								
							}else {
								
								System.out.print("\nIngresa 0 para continuar: ");
								int continuar2 = sc2.nextInt();
								while (nroCafes > 0) {
									pedido.add(new Cafe());
									Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
									nroCafes --;}
								while (nroJugos > 0) {
									pedido.add(new Jugo());
									Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
									nroJugos --;}
								System.out.println(elegido.prepararVenta(pedido, cliente, domiciliario, promocion));
								System.out.print("\nIngresa 0 para continuar: ");
								int continuar3 = sc2.nextInt();
							}
							
						}else {
							System.out.println("El pedido no cumplía con los requisitos de la promoción");
						}
					}else if(x == 2) {
						if(nroJugos >= 2) {
							promocion = Promocion.JUGO2X1;
							Random r = new Random();
							int randomNumber = r.nextInt(Domiciliario.getDomiciliarios().size());
							Domiciliario domiciliario = Domiciliario.getDomiciliarios().get(randomNumber);
							System.out.println(domiciliario.toString());
							if (domiciliario.isIncidentes()) {
							System.out.print("\nIngresa 0 para rechazar la orden o 1 para continuar, ignorando el reporte: ");
							int continuar2 = sc2.nextInt();
							if (continuar2 == 1) {
								while (nroCafes > 0) {
									pedido.add(new Cafe());
									Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
									nroCafes --;}
								while (nroJugos > 0) {
									pedido.add(new Jugo());
									Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
									nroJugos --;}
								System.out.println(elegido.prepararVenta(pedido, cliente, domiciliario, promocion));
								System.out.print("\nIngresa 0 para continuar: ");
								int continuar3 = sc2.nextInt();
							}
								
							}else {
								
								System.out.print("\nIngresa 0 para continuar: ");
								int continuar2 = sc2.nextInt();
								while (nroCafes > 0) {
									pedido.add(new Cafe());
									Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
									nroCafes --;}
								while (nroJugos > 0) {
									pedido.add(new Jugo());
									Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
									nroJugos --;}
								System.out.println(elegido.prepararVenta(pedido, cliente, domiciliario, promocion));
								System.out.print("\nIngresa 0 para continuar: ");
								int continuar3 = sc2.nextInt();
							}
						}else {
							System.out.println("El pedido no cumplía con los requisitos de la promoción");
						}
					} else if(x == 3) {
						if(nroCafes >= 1 && nroJugos >= 1) {
							promocion = Promocion.CAFECONJUGOAL50;
							Random r = new Random();
							int randomNumber = r.nextInt(Domiciliario.getDomiciliarios().size());
							Domiciliario domiciliario = Domiciliario.getDomiciliarios().get(randomNumber);
							System.out.println(domiciliario.toString());
							if (domiciliario.isIncidentes()) {
							System.out.print("\nIngresa 0 para rechazar la orden o 1 para continuar, ignorando el reporte: ");
							int continuar2 = sc2.nextInt();
							if (continuar2 == 1) {
								while (nroCafes > 0) {
									pedido.add(new Cafe());
									Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
									nroCafes --;}
								while (nroJugos > 0) {
									pedido.add(new Jugo());
									Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
									nroJugos --;}
								System.out.println(elegido.prepararVenta(pedido, cliente, domiciliario, promocion));
								System.out.print("\nIngresa 0 para continuar: ");
								int continuar3 = sc2.nextInt();
							}
								
							}else {
								
								System.out.print("\nIngresa 0 para continuar: ");
								int continuar2 = sc2.nextInt();
								while (nroCafes > 0) {
									pedido.add(new Cafe());
									Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
									nroCafes --;}
								while (nroJugos > 0) {
									pedido.add(new Jugo());
									Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
									nroJugos --;}
								System.out.println(elegido.prepararVenta(pedido, cliente, domiciliario, promocion));
								System.out.print("\nIngresa 0 para continuar: ");
								int continuar3 = sc2.nextInt();
							}
						}else {
							System.out.println("El pedido no cumplía con los requisitos de la promoción");
						}
				}else{
					Random r = new Random();
					int randomNumber = r.nextInt(Domiciliario.getDomiciliarios().size());
					Domiciliario domiciliario = Domiciliario.getDomiciliarios().get(randomNumber);
					System.out.println(domiciliario.toString());
					if (domiciliario.isIncidentes()) {
					System.out.print("\nIngresa 0 para rechazar la orden o 1 para continuar, ignorando el reporte: ");
					int continuar2 = sc2.nextInt();
					if (continuar2 == 1) {
						while (nroCafes > 0) {
							pedido.add(new Cafe());
							Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
							nroCafes --;}
						while (nroJugos > 0) {
							pedido.add(new Jugo());
							Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
							nroJugos --;}
						System.out.println(elegido.prepararVenta(pedido, cliente, domiciliario));
						System.out.print("\nIngresa 0 para continuar: ");
						int continuar3 = sc2.nextInt();
					}
						
					}else {
						
						System.out.print("\nIngresa 0 para continuar: ");
						int continuar2 = sc2.nextInt();
						while (nroCafes > 0) {
							pedido.add(new Cafe());
							Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
							nroCafes --;}
						while (nroJugos > 0) {
							pedido.add(new Jugo());
							Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
							nroJugos --;}
						System.out.println(elegido.prepararVenta(pedido, cliente, domiciliario));
						System.out.print("\nIngresa 0 para continuar: ");
						int continuar3 = sc2.nextInt();
					}}
			}
				else{
					
					
					Random r = new Random();
					int randomNumber = r.nextInt(Domiciliario.getDomiciliarios().size());
					Domiciliario domiciliario = Domiciliario.getDomiciliarios().get(randomNumber);
					System.out.println(domiciliario.toString());
					if (domiciliario.isIncidentes()) {
					System.out.print("\nIngresa 0 para rechazar la orden o 1 para continuar, ignorando el reporte: ");
					int continuar2 = sc2.nextInt();
					if (continuar2 == 1) {
						while (nroCafes > 0) {
							pedido.add(new Cafe());
							Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
							nroCafes --;}
						while (nroJugos > 0) {
							pedido.add(new Jugo());
							Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
							nroJugos --;}
						System.out.println(elegido.prepararVenta(pedido, cliente, domiciliario));
						System.out.print("\nIngresa 0 para continuar: ");
						int continuar3 = sc2.nextInt();
					}
						
					}else {
						
						System.out.print("\nIngresa 0 para continuar: ");
						int continuar2 = sc2.nextInt();
						while (nroCafes > 0) {
							pedido.add(new Cafe());
							Cafe.setInventarioCafe(Cafe.getInventarioCafe()-2);
							nroCafes --;}
						while (nroJugos > 0) {
							pedido.add(new Jugo());
							Jugo.setInventarioJugo(Jugo.getInventarioJugo()-2);
							nroJugos --;}
						System.out.println(elegido.prepararVenta(pedido, cliente, domiciliario));
						System.out.print("\nIngresa 0 para continuar: ");
						int continuar3 = sc2.nextInt();
					}
					
					}	
			}
			else {
				System.out.println("No hay suficientes jugos para completar la orden");
				
			}
			
		}else {
			System.out.println("No hay suficientes cafés para completar la orden");
			
		
	}
	
	
	}
}
