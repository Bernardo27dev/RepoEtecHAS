package br.com.etechoracio.study.controller;

import br.com.etechoracio.study.entity.Disciplina;
import br.com.etechoracio.study.entity.Monitor;
import br.com.etechoracio.study.service.DisciplinaService;
import br.com.etechoracio.study.service.MonitorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/monitores")
public class MonitorController {
    @Autowired
    private MonitorService service;
    @PostMapping("/cadastrar")
    public ResponseEntity<Monitor> cadastrarMonitor(@RequestBody Monitor monitor){
        var newMonitor = service.cadastrarMonitor(monitor);
        return ResponseEntity.status(HttpStatus.CREATED).body(newMonitor);
        
    }
}
