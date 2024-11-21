package br.com.etechoracio.study.controller;

import br.com.etechoracio.study.entity.Disciplina;
import br.com.etechoracio.study.service.DisciplinaService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/disciplinas")
public class DisciplinaController {
    @Autowired
    private DisciplinaService service;
    @GetMapping
    public List<Disciplina> listar(){
        return service.listar();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Disciplina> buscarPorId(@PathVariable Long id){
        var existe = service.buscarPorId(id);
        if(existe.isPresent()){
            return ResponseEntity.ok(existe.get());
        }
        else{
            return ResponseEntity.notFound().build();
        }
        /*
        return service.buscarPorId(id)
                .map(d-> ResponseEntity.ok(d))
                .orElse(ResponseEntity.notFound().build());
         */
    }
    @PostMapping
    public ResponseEntity<Disciplina> cadastrar(@RequestBody Disciplina disciplina){
        var novaDisciplina = service.cadastrarDisciplina(disciplina);
        return ResponseEntity.status(HttpStatus.CREATED).body(novaDisciplina);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Disciplina> atualizar(@PathVariable Long id,
                                @RequestBody Disciplina disciplina){
        Disciplina atualizado = new Disciplina();
        var existe = service.buscarPorId(id);
        if(existe.isPresent()){
            atualizado = service.atualizar(disciplina);
            return ResponseEntity.ok(atualizado);
        }
        else{
            return ResponseEntity.notFound().build();
        }


    }

    @DeleteMapping("/{id}")
    public void excluir(@PathVariable Long id){
        var existe = service.buscarPorId(id);
        if(existe.isPresent()){
            service.excluir(existe.get());
        }
    }
}
