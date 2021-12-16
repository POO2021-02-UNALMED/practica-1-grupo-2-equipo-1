package uiMain;

import java.util.Scanner;

import gestorAplicacion.noPersonas.Cafe;
import gestorAplicacion.noPersonas.Jugo;

public class Inventario {
	
	public static void start() {
		Scanner sc = new Scanner(System.in);
		System.out.println("\nEn este momento hay:\n\n"+ Cafe.getInventarioCafe()+" Cafés\n"+ Jugo.getInventarioJugo() +" Jugos\n");
		System.out.print("Ingrese 0 para continuar: ");
		int i = sc.nextInt();
	}
}
