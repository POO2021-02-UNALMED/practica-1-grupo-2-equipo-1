package uiMain;
import java.util.Scanner;

import gestorAplicacion.noPersonas.Orden;
import gestorAplicacion.personas.*;
public class HistoricoVentas {

	
	public static void start() {
		System.out.println("\nHasta el momento las ventas han sido:");
		for(Barista x: Barista.getBaristas()) {
			for(Orden y: x.getOrdenes()) {
				System.out.println(y.toString());
			}
		}
		Scanner sc = new Scanner(System.in);
		System.out.print("\nIngrese 0 para continuar: ");
		int i = sc.nextInt();
	}
}
