package uiMain;

import java.util.Scanner;

public class ActivarPromocion {
	private static boolean promos = false;
	public static void start() {
		if (promos == false) {
		Scanner sc = new Scanner(System.in);
		System.out.print("\n¿Estás seguro que quieres activar las promociones?\n\n0. No\n1. Sí\n\nIngresa 0 o 1 respectivamente: ");
		int i = sc.nextInt();
		if (i == 0) {
			System.out.println("\nNo se han activado las promociones");
			System.out.print("\nIngresa 0 para continuar: ");
			int e = sc.nextInt();
		} else {
			System.out.println("\nSe han activado las promociones");
			promos = true;
			System.out.print("\nIngresa 0 para continuar: ");
			int e = sc.nextInt();
		}}else {
			Scanner sc = new Scanner(System.in);
			System.out.println("\nLas promociones ya están activas");
			System.out.print("\nIngresa 0 para continuar: ");
			int e = sc.nextInt();
		}
		
	}
	public static boolean isPromos() {
		return promos;
	}
	public static void setPromos(boolean promos) {
		ActivarPromocion.promos = promos;
	}
}
