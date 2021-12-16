package uiMain;
import java.util.Scanner;
import gestorAplicacion.personas.*;
public class ConsultarComision {
		
	public static void start() {
		System.out.println("\nEn este momento los baristas tienen las siguientes comisiones:");
		for(Barista x: Barista.getBaristas()) {
			System.out.println("\n" + x.getNombre() + " comisiona al " + x.getComisionAcumulada() +  "% y ha comisionado " + x.getComisionVentas());}
			Scanner sc = new Scanner(System.in);
			System.out.print("\nIngrese 0 para continuar: ");
			int i = sc.nextInt();
		
	}
}
