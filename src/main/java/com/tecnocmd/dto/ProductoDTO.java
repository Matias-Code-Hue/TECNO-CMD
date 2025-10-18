// ProductoDTO.java

package com.tecnocmd.dto;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public class ProductoDTO {
    @NotBlank
    private String nombre;

    @NotBlank
    private String marca;

    @NotNull @Min(0)
    private Double precio;

    @NotNull @Min(0)
    private Integer stock;

    private String especificaciones;

    public ProductoDTO() {}

    public ProductoDTO(String nombre, String marca, Double precio, Integer stock, String especificaciones) {
        this.nombre = nombre;
        this.marca = marca;
        this.precio = precio;
        this.stock = stock;
        this.especificaciones = especificaciones;
    }

    // getters y setters
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getMarca() { return marca; }
    public void setMarca(String marca) { this.marca = marca; }

    public Double getPrecio() { return precio; }
    public void setPrecio(Double precio) { this.precio = precio; }

    public Integer getStock() { return stock; }
    public void setStock(Integer stock) { this.stock = stock; }

    public String getEspecificaciones() { return especificaciones; }
    public void setEspecificaciones(String especificaciones) { this.especificaciones = especificaciones; }
}
