package baseDatos;

import java.util.ArrayList;

import gestorAplicacion.personas.*;
import gestorAplicacion.noPersonas.*;

import java.io.EOFException;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;
import java.io.FileNotFoundException;

public class Serializar {
	public ArrayList<Empleado> empleados = new ArrayList<>(); 
	public ArrayList<Domiciliario> domiciliarios = new ArrayList<>(); 
	
	public void serializarEmp () {
		
		FileOutputStream fileOut;
		
		try {
			fileOut = new FileOutputStream(new File(System.getProperty("user.dir") + "\\src\\adm.txt"));
			ObjectOutputStream out = new ObjectOutputStream(fileOut);
			
			for (Empleado i : empleados) {
				out.writeObject(i);
			}
						
			out.close();
			fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void serializarDom () {
		
		FileOutputStream fileOut;
		
		try {
			fileOut = new FileOutputStream(new File(System.getProperty("user.dir") + "\\src\\dm.txt"));
			ObjectOutputStream out = new ObjectOutputStream(fileOut);
			
			for (Domiciliario i : domiciliarios) {
				out.writeObject(i);
			}
						
			out.close();
			fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void deserializarEmp () {
		FileInputStream fileIn;
		try {
			fileIn = new FileInputStream(new File(System.getProperty("user.dir") +"\\src\\adm.txt"));
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			ArrayList<Empleado> listado =  new ArrayList<>();
			
			try {
				Object obj = in.readObject();
				
				while(obj != null) {
					
					listado.add((Empleado)obj);
					
					obj = in.readObject();
				}
				
				
			} catch (EOFException e) {
				// TODO Auto-generated catch block
			}
			
			//
			for (Object i : listado) {
				System.out.println(i.toString());
			}
			
	        in.close();
	        fileIn.close();
	        
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void deserializarDom () {
		FileInputStream fileIn;
		try {
			fileIn = new FileInputStream(new File(System.getProperty("user.dir") +"\\src\\dm.txt"));
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			ArrayList<Domiciliario> listado =  new ArrayList<>();
			
			try {
				Object obj = in.readObject();
				
				while(obj != null) {
					
					listado.add((Domiciliario)obj);
					
					obj = in.readObject();
				}
				
				
			} catch (EOFException e) {
				// TODO Auto-generated catch block
			}
			
			//
			for (Object i : listado) {
				System.out.println(i.toString());
			}
			
	        in.close();
	        fileIn.close();
	        
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

