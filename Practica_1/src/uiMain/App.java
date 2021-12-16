package uiMain;

import java.util.Scanner;
import gestorAplicacion.noPersonas.*;
import gestorAplicacion.personas.*;
import java.util.ArrayList;
import baseDatos.Serializar;

public class App {


	public static void main(String[] args) {
		
		System.out.println("Bienvenido al sistema Auros");
		Cafe.prepararCafes(5);
		Jugo.prepararJugos(5);
		
		Serializar s = new Serializar();
		Administrador admin = new Administrador(0,"Admin",0, "Admin", "0000");
		s.empleados.add(admin);
		Barista bar1 = new Barista(100988877,"Julio C�rdenas");
		s.empleados.add(bar1);
		Barista bar2 = new Barista(100844433,"Stephanie Per�z");
		s.empleados.add(bar2);
		Barista bar3 = new Barista(100344521,"Camilo Montaner");
		s.empleados.add(bar3);
		Domiciliario dom1 = new Domiciliario("Santiago Monsalve");
		s.domiciliarios.add(dom1);
		Domiciliario dom2 = new Domiciliario("Hern�n Cort�z");
		s.domiciliarios.add(dom1);
		Domiciliario dom3 = new Domiciliario("Juan Gom�z");
		s.domiciliarios.add(dom1);
		
		s.serializarEmp();
		s.serializarDom();
		
		while(true) {
			Scanner sc = new Scanner(System.in);
			
			System.out.print("\nIntroduce tu usuario: ");
			String usuario = sc.nextLine();
			if (usuario.equals(admin.getUsuario())) {
				System.out.print("Introduce tu contrase�a: ");
				String contrasena = sc.nextLine();
				if (contrasena.equals(admin.getContrasena())) {
					break;
				}else {
					System.out.println("La contrase�a que ha ingresado no es v�lida, intente de nuevo");
					
				}
			} else {
				System.out.println("El usuario ingresado no es v�lido, intente de nuevo");
			}
		}
		
		while(true) {
			Scanner sc = new Scanner(System.in);
			System.out.print("\nElige lo que quieres hacer a continuacion:\n"
					+ "\n1. Registrar una venta"
					+ "\n2. Activar las promociones"
					+ "\n3. Reportar incidente con un domiciliario"
					+ "\n4. Consultar comisiones de los baristas"
					+ "\n5. Consultar hist�rico de ventas"
					+ "\n6. Preparar caf�s"
					+ "\n7. Preparar jugos"
					+ "\n8. Consultar bebidas en inventario"
					+ "\n9. Salir"
					+ "\n\nEscribe el n�mero de la opci�n que deseas: ");
			int eleccion = sc.nextInt();
			
			switch(eleccion) {
			case 1: registroVenta.start();
					continue;
			case 2: ActivarPromocion.start();
					continue;
			case 3: ReportarIncidente.start();
					continue;
			case 4: ConsultarComision.start();
					continue;
			case 5: HistoricoVentas.start();
					continue;
			case 6: PrepararCafe.start();
					continue;
			case 7: PrepararJugo.start();
					continue;
			case 8: Inventario.start();
					continue;
			case 9: break;
			default: System.out.println("Esa no es una opci�n v�lida, intenta de nuevo");
					continue;
			}
			break;
			
		}
		
		s.deserializarEmp();
		s.deserializarDom();
	}

}
