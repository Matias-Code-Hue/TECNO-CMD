// ProductoService.java

package com.tecnocmd.service;

import com.tecnocmd.dto.ProductoDTO;
import com.tecnocmd.model.Producto;
import com.tecnocmd.repository.ProductoRepository;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class ProductoService {
    private final ProductoRepository repo;

    public ProductoService(ProductoRepository repo) {
        this.repo = repo;
    }

    public List<Producto> listarTodos() { return repo.findAll(); }

    public Producto obtenerPorId(Integer id) {
        return repo.findById(id).orElse(null);
    }

    public List<Producto> buscarPorMarca(String marca) {
        return repo.findByMarcaIgnoreCase(marca);
    }

    public Producto crearProducto(ProductoDTO dto) {
        Producto p = new Producto(dto.getNombre(), dto.getMarca(), dto.getPrecio(), dto.getStock(), dto.getEspecificaciones());
        return repo.save(p);
    }

    public Producto actualizarProducto(Integer id, ProductoDTO dto) {
        Producto existente = repo.findById(id).orElse(null);
        if (existente == null) return null;

        existente.setNombre(dto.getNombre());
        existente.setMarca(dto.getMarca());
        existente.setPrecio(dto.getPrecio());
        existente.setStock(dto.getStock());
        existente.setEspecificaciones(dto.getEspecificaciones());

        return repo.save(existente);
    }

    public boolean eliminarProducto(Integer id) {
        if (!repo.existsById(id)) return false;
        repo.deleteById(id);
        return true;
    }
}