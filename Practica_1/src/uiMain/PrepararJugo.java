package uiMain;

import java.util.Scanner;

import gestorAplicacion.noPersonas.Jugo;

public class PrepararJugo {
	
	public static void start() {
		Scanner sc = new Scanner(System.in);
		System.out.println("\n¿Cuántos jugos van a preparar?");
		int jugos = sc.nextInt();
		Jugo.prepararJugos(jugos);
		System.out.println("\nSe prepararon " + jugos + " jugos.");
		System.out.print("\nIngrese 0 para continuar: ");
		int continuar = sc.nextInt();
	}
}
