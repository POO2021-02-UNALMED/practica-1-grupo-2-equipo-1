package uiMain;

import java.util.Scanner;

import gestorAplicacion.noPersonas.OrdenVirtual;

public class ReportarIncidente {

	
		public static void start() {
			Scanner sc = new Scanner(System.in);
			System.out.println("\n¿De cuál órden virtual quieres reportar un incidente?\n");
			for (int i = 0; i<OrdenVirtual.getOrdenesVirtuales().size();i++) {
				System.out.println((i+1) + ". Orden "+OrdenVirtual.getOrdenesVirtuales().get(i).getNroOrden());
			}
			System.out.print("\nIngresa el número correspondiente a la\n orden del domiciliario que quieres reportar: ");
			int e = sc.nextInt();
			OrdenVirtual.getOrdenesVirtuales().get(e-1).reportarIncidente();
			System.out.print("\nEl domiciliario ha sido reportado\n\nIngresa 0 para continuar: ");
			int y = sc.nextInt();
			
		}
}
