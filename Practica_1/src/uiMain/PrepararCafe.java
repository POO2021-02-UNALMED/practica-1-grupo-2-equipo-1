package uiMain;
import java.util.Scanner;

import gestorAplicacion.noPersonas.*;
public class PrepararCafe {

	public static void start() {
		Scanner sc = new Scanner(System.in);
		System.out.println("\n�Cu�ntos caf�s van a preparar?");
		int cafes = sc.nextInt();
		Cafe.prepararCafes(cafes);
		System.out.println("\nSe prepararon " + cafes + " caf�s.");
		System.out.print("\nIngrese 0 para continuar: ");
		int continuar = sc.nextInt();
	}
}
