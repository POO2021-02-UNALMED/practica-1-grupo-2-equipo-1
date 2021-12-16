package uiMain;
import java.util.Scanner;

import gestorAplicacion.noPersonas.*;
public class PrepararCafe {

	public static void start() {
		Scanner sc = new Scanner(System.in);
		System.out.println("\n¿Cuántos cafés van a preparar?");
		int cafes = sc.nextInt();
		Cafe.prepararCafes(cafes);
		System.out.println("\nSe prepararon " + cafes + " cafés.");
		System.out.print("\nIngrese 0 para continuar: ");
		int continuar = sc.nextInt();
	}
}
